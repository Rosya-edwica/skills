package db

import (
	"fmt"
	"skills/models"
	"skills/tools"
)

func (d *DB) GetSkills() (skills []models.Skill) {
	rows, err := d.Connection.Query("SELECT id, name FROM demand WHERE type_group='навык' AND is_deleted IS FALSE")
	tools.CheckErr(err)
	defer rows.Close()
	for rows.Next() {
		var id int
		var name string
		err = rows.Scan(&id, &name)
		tools.CheckErr(err)
		skills = append(skills, models.Skill{
			Id:   id,
			Name: name,
		})
	}
	return
}

func (d *DB) UpdateSkillsAfterSpeller(skills []models.FixedSkill) {
	for _, skill := range skills {
		query := fmt.Sprintf(`UPDATE demand SET name='%s' WHERE id=%d;`, skill.FixedName, skill.Id)
		tx, _ := d.Connection.Begin()
		_, err := d.Connection.Exec(query)
		tools.CheckErr(err)
		tx.Commit()
		fmt.Println("Успешно обновили навык №", skill.Id)
	}
}
