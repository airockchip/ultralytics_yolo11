# Ultralytics YOLO 🚀, AGPL-3.0 license

from pathlib import Path

from ultralytics.cfg import cfg2dict, check_dict_alignment

from .ai_gym import AIGym
from .analytics import Analytics
from .distance_calculation import DistanceCalculation
from .heatmap import Heatmap
from .object_counter import ObjectCounter
from .parking_management import ParkingManagement, ParkingPtsSelection
from .queue_management import QueueManager
from .speed_estimation import SpeedEstimator
from .streamlit_inference import inference

__all__ = (
    "AIGym",
    "DistanceCalculation",
    "Heatmap",
    "ObjectCounter",
    "ParkingManagement",
    "ParkingPtsSelection",
    "QueueManager",
    "SpeedEstimator",
    "Analytics",
)


def solutions_yaml_load(kwargs):
    args = cfg2dict(Path(__file__).resolve().parents[0] / "cfg/default.yaml")
    check_dict_alignment(args, kwargs)
    return args
