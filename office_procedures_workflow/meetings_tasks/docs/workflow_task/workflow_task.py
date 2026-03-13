"""Doc runtime hooks for workflow_task."""

class DocRuntime:
    doc_key = "workflow_task"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close', 'archive']
