import json, logging, sys


class JsonFormatter(logging.Formatter):
    def format(self, record):
        extra = getattr(record, "__dict__", {})
        json_record = {
            "Time": self.formatTime(record),
            "Level": getattr(record, "levelname", None),
            "File": getattr(record, "filename", None),
            "Line": getattr(record, "lineno", None),
            "Msg": getattr(record, "msg", None),
            "additional_detail": extra.get("additional_detail"),
        }
        return json.dumps(json_record)


def jsonConfig(filename=None):
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    logging.getLogger().addHandler(handler)