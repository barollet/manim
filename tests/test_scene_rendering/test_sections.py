from __future__ import annotations

import sys

import pytest

from manim import capture
from tests.assert_utils import assert_dir_exists, assert_dir_not_exists

from ..utils.video_tester import video_comparison
from .simple_scenes import SceneWithGroupAPI, SceneWithGroupList, SquareToCircle


@pytest.mark.slow
@video_comparison(
    "SceneWithDisabledSections.json",
    "videos/simple_scenes/480p15/SquareToCircle.mp4",
)
def test_no_sections(tmp_path, manim_cfg_file, simple_scenes_path):
    scene_name = "SquareToCircle"
    command = [
        sys.executable,
        "-m",
        "manim",
        "-ql",
        "--media_dir",
        str(tmp_path),
        str(simple_scenes_path),
        scene_name,
    ]
    _, err, exit_code = capture(command)
    assert exit_code == 0, err

    scene_dir = tmp_path / "videos" / "simple_scenes" / "480p15"
    assert_dir_exists(scene_dir)
    assert_dir_not_exists(scene_dir / "sections")


@pytest.mark.slow
@video_comparison(
    "SceneWithEnabledSections.json",
    "videos/simple_scenes/480p15/SquareToCircle.mp4",
)
def test_sections(tmp_path, manim_cfg_file, simple_scenes_path):
    scene_name = "SquareToCircle"
    command = [
        sys.executable,
        "-m",
        "manim",
        "-ql",
        "--save_sections",
        "--media_dir",
        str(tmp_path),
        str(simple_scenes_path),
        scene_name,
    ]
    _, err, exit_code = capture(command)
    assert exit_code == 0, err

    scene_dir = tmp_path / "videos" / "simple_scenes" / "480p15"
    assert_dir_exists(scene_dir)
    assert_dir_exists(scene_dir / "sections")


@pytest.mark.slow
@video_comparison(
    "SceneWithSections.json",
    "videos/simple_scenes/480p15/SceneWithSections.mp4",
)
def test_many_sections(tmp_path, manim_cfg_file, simple_scenes_path):
    scene_name = "SceneWithSections"
    command = [
        sys.executable,
        "-m",
        "manim",
        "-ql",
        "--save_sections",
        "--media_dir",
        str(tmp_path),
        str(simple_scenes_path),
        scene_name,
    ]
    _, err, exit_code = capture(command)
    assert exit_code == 0, err


@pytest.mark.slow
@video_comparison(
    "SceneWithSkipAnimations.json",
    "videos/simple_scenes/480p15/ElaborateSceneWithSections.mp4",
)
def test_skip_animations(tmp_path, manim_cfg_file, simple_scenes_path):
    scene_name = "ElaborateSceneWithSections"
    command = [
        sys.executable,
        "-m",
        "manim",
        "-ql",
        "--save_sections",
        "--media_dir",
        str(tmp_path),
        str(simple_scenes_path),
        scene_name,
    ]
    _, err, exit_code = capture(command)
    assert exit_code == 0, err


def test_groups_api(tmp_path):
    find_api_scene = SceneWithGroupAPI()
    list_api_scene = SceneWithGroupList()

    assert not SquareToCircle().section_groups
    assert len(list_api_scene.section_groups) == len(find_api_scene.section_groups) == 2
    assert (
        list_api_scene.section_groups[0].func.__name__
        == find_api_scene.section_groups[0].func.__name__
        == "transform"
    )
    assert (
        list_api_scene.section_groups[1].func.__name__
        == find_api_scene.section_groups[1].func.__name__
        == "back_transform"
    )
