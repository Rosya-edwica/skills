package speller

import (
	"fmt"
	"skills/logger"
	"skills/models"
	"strings"
	"sync"
)

const POOLS_LIMIT = 1000

func StartChecking(skills []models.Skill) (fixedSkills []models.FixedSkill) {
	grouped_skills := groupSkills(skills)
	fmt.Println(len(grouped_skills))
	for i, group := range grouped_skills {
		fixedSkills = append(fixedSkills, correctAllSkills(group)...)
		fmt.Println("group: ", i)
	}
	return
}

func groupSkills(skills []models.Skill) (grouped_skills [][]models.Skill) {
	for i := 0; i < len(skills); i += POOLS_LIMIT {
		group := skills[i:]
		if len(group) >= POOLS_LIMIT {
			grouped_skills = append(grouped_skills, group[:POOLS_LIMIT])
		} else {
			grouped_skills = append(grouped_skills, group)
		}
	}
	return
}

func correctAllSkills(skills []models.Skill) (fixedSkills []models.FixedSkill) {
	var wg sync.WaitGroup
	wg.Add(len(skills))

	for _, skill := range skills {
		go correct(skill, &wg, &fixedSkills)
	}
	wg.Wait()
	return
}

func correct(skill models.Skill, wg *sync.WaitGroup, skills *[]models.FixedSkill) {
	correctedSkill := strings.Clone(skill.Name)
	wrongWords := CheckText(skill.Name)
	for _, word := range wrongWords {
		correctedSkill = strings.ReplaceAll(correctedSkill, word.WrongVersion, word.CorrectVersion[0])
	}
	if correctedSkill != skill.Name {
		*skills = append(*skills, models.FixedSkill{
			Id:        skill.Id,
			Name:      skill.Name,
			FixedName: correctedSkill,
		})
		logger.Log.Printf("Ошибка - %s -> %s", skill.Name, correctedSkill)
	} else {
		logger.Log.Printf("Нет ошибок - %s", skill.Name)
	}
	wg.Done()
}
