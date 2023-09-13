package speller

import (
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"net/url"
	"skills/models"
	"time"
)

func CheckText(text string) (correctedSlice []models.WrongSkillJson) {
	generatedUrl := generateParamsUrl(text)
	req, err := http.Get(generatedUrl)
	if err != nil {
		fmt.Println("Словили ошибку. Теперь отдыхаем 30 секунд.")
		time.Sleep(30 * time.Second)

	}
	if req.StatusCode != 200 {
		return
	}
	correctedSlice = parseJson(req.Body)
	return
}

func generateParamsUrl(paramsText string) (urlWithParams string) {
	params := url.Values{}
	params.Add("text", paramsText)
	params.Add("lang", "ru, en")
	urlWithParams = "https://speller.yandex.net/services/spellservice.json/checkText?" + params.Encode()
	return
}

func parseJson(data io.ReadCloser) (result []models.WrongSkillJson) {
	// распаковываем массив
	body, err := ioutil.ReadAll(data)
	checkErr(err)
	err = json.Unmarshal(body, &result)
	checkErr(err)
	return

}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
