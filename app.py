import os
from agents.plot_agent import PlotAgent
from agents.character_agent import CharacterAgent
from agents.setting_agent import SettingAgent
from agents.dialogue_agent import DialogueAgent
from agents.conflict_agent import ConflictAgent
from agents.editor_agent import EditorAgent

plot_agent = PlotAgent()
character_agent = CharacterAgent()
setting_agent = SettingAgent()
dialogue_agent = DialogueAgent()
conflict_agent = ConflictAgent()
editor_agent = EditorAgent()


def run_story_workflow(topic):
    print("Running story generation workflow...")
    
    print("Step 1: Developing plot...")
    plot_content = plot_agent.develop_plot(topic)
    print(f"Plot developed: {len(plot_content)} characters")
    
    print("Step 2: Developing characters...")
    character_content = character_agent.develop_characters(plot_content)
    print(f"Characters developed: {len(character_content)} characters")
    
    print("Step 3: Creating setting...")
    setting_content = setting_agent.create_setting(character_content, plot_content)
    print(f"Setting created: {len(setting_content)} characters")
    
    print("Step 4: Generating conflicts...")
    conflict_content = conflict_agent.generate_conflicts(setting_content, character_content)
    print(f"Conflicts generated: {len(conflict_content)} characters")
    
    print("Step 5: Writing dialogue...")
    dialogue_content = dialogue_agent.write_dialogue(conflict_content, setting_content)
    print(f"Dialogue written: {len(dialogue_content)} characters")
    
    print("Step 6: Final editing...")
    final_story = editor_agent.edit_story(dialogue_content, conflict_content)
    print(f"Final story: {len(final_story)} characters")
    
    return final_story

if __name__ == "__main__":
    topic = "In a world where magic has been outlawed, a young sorcerer discovers an ancient artifact that could change everything."
    
    print("=" * 80)
    print("TALE-AI: AI-Powered Story Generation")
    print("=" * 80)
    print(f"Topic: {topic}")
    print("=" * 80)
    
    
    final_story = run_story_workflow(topic)
    
    print("\n" + "=" * 80)
    print("FINAL STORY")
    print("=" * 80)
    print(final_story)
    print("=" * 80)