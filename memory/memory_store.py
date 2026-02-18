import json
import os
from datetime import datetime


class SharedMemory:
    def __init__(self, filepath="system_memory.json"):
        self.filepath = filepath
        self.state = {
            "run_id": None,
            # Core system state
            "goal": None,
            "pm_output": None,
            "tech_plan": None,
            "final_plan": None,

            # Versioned artifacts
            "dev_versions": [],
            "critic_reviews": [],
            "critic_scores": [],
            "iteration_history": [],

            # Legacy fields (keep so nothing breaks)
            "iterations": [],
            "current_code": None,
            "qa_feedback": [],
            
            #architecture and risks
            "architecture": None,
            "risks": None,
    

            # System logs
            "history": []
        }
        self._load()

    # -----------------------------
    # Load memory from disk safely
    # -----------------------------
    def _load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    self.state = json.load(f)
            except Exception:
                print("[Memory] Corrupted file detected. Resetting memory.")
                self._save()

    # -----------------------------
    # Save memory to disk
    # -----------------------------
    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.state, f, indent=4)

    # -----------------------------
    # Update single value
    # -----------------------------
    def update(self, key, value):
        self.state[key] = value
        self._log_history(key, "update")
        self._save()

    # -----------------------------
    # Append to list-based memory
    # -----------------------------
    def append(self, key, value):
        if key not in self.state or not isinstance(self.state[key], list):
            self.state[key] = []
        self.state[key].append(value)
        self._log_history(key, "append")
        self._save()

    # -----------------------------
    # Retrieve value
    # -----------------------------
    def get(self, key, default=None):
        return self.state.get(key, default)

    # -----------------------------
    # Store critic score separately
    # -----------------------------
    def add_score(self, score):
        self.state["critic_scores"].append({
            "score": score,
            "timestamp": datetime.now().isoformat()
        })
        self._log_history("critic_scores", "append")
        self._save()

    # -----------------------------
    # Snapshot entire system state
    # Useful for demo + resume
    # -----------------------------
    def snapshot(self):
        return self.state.copy()

    # -----------------------------
    # Reset system memory
    # Useful during testing
    # -----------------------------
    def reset(self):
        os.remove(self.filepath) if os.path.exists(self.filepath) else None
        self.__init__(self.filepath)

    # -----------------------------
    # Internal logging
    # -----------------------------
    def _log_history(self, key, action):
        self.state["history"].append({
            "timestamp": datetime.now().isoformat(),
            "field": key,
            "action": action
        })
