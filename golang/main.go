package main

import (
	"os"
	"skills/db"
	"skills/speller"
	"skills/tools"

	"github.com/joho/godotenv"
)

func main() {
	database := initDatabase()
	skills := database.GetSkills()
	fixed := speller.StartChecking(skills)
	database.UpdateSkillsAfterSpeller(fixed)
	database.Close()
}

func initDatabase() (database *db.DB) {
	err := godotenv.Load("../.env")
	tools.CheckErr(err)
	database = &db.DB{Host: os.Getenv("MYSQL_HOST"),
		User: os.Getenv("MYSQL_USER"),
		Name: os.Getenv("MYSQL_DATABASE"),
		Pass: os.Getenv("MYSQL_PASSWORD"),
		Port: os.Getenv("MYSQL_PORT"),
	}
	database.Connection = database.Connect()
	return
}
