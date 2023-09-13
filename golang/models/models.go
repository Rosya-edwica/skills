package models

type Skill struct {
	Id   int
	Name string
}
type FixedSkill struct {
	Id        int
	Name      string
	FixedName string
}

type WrongSkillJson struct {
	WrongVersion   string   `json:"word"`
	CorrectVersion []string `json:"s"`
}
