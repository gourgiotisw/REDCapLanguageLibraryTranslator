# REDCap Language Library Translator

## Overview

The REDCap Language Library Translator is a Python script designed to translate the "default" values in a REDCap JSON file  into a user-defined language using the Google Translate API. The script handles large text translations by breaking them into manageable chunks and also manages translation errors by logging them into a separate file.

## Features

- **Language Support:** Translates "default" values into a wide range of languages.
- **Chunk Processing:** Handles large texts by breaking them into smaller chunks.
- **Error Handling:** Logs any translation errors into a separate file.
- **JSON Key Updates:** Updates the `display` and `key` fields in the JSON file to reflect the new language.

## Supported Languages

| Supported Languages        |      |       |
|----------------------------|----------------------------|----------------------------|
| Afrikaans                  | Haitian Creole             | Pashto                     |
| Amharic                    | Hebrew                     | Persian (Farsi)            |
| Arabic                     | Hindi                      | Polish                     |
| Azerbaijani                | Hungarian                  | Portuguese                 |
| Bashkir                    | Icelandic                  | Punjabi                    |
| Belarusian                 | Indonesian                 | Queretaro Otomi            |
| Bengali                    | Irish                      | Romanian                   |
| Bosnian                    | Italian                    | Russian                    |
| Bulgarian                  | Japanese                   | Samoan                     |
| Catalan                    | Kannada                    | Scots Gaelic               |
| Cebuano                    | Kazakh                     | Serbian                    |
| Chinese (Simplified)       | Khmer                      | Slovak                     |
| Chinese (Traditional)      | Klingon (TlhIngan Hol)     | Slovenian                  |
| Chuvash                    | Korean                     | Spanish                    |
| Croatian                   | Kurdish                    | Swahili                    |
| Czech                      | Kyrgyz                     | Swedish                    |
| Danish                     | Lao                        | Tajik                      |
| Dutch                      | Latvian                    | Tamil                      |
| English                    | Lithuanian                 | Telugu                     |
| Esperanto                  | Luxembourgish              | Thai                       |
| Estonian                   | Macedonian                 | Tongan                     |
| Fijian                     | Malagasy                   | Turkish                    |
| Filipino                   | Malay                      | Turkmen                    |
| Finnish                    | Maltese                    | Ukrainian                  |
| French                     | Mongolian                  | Urdu                       |
| Georgian                   | Nepali                     | Uyghur                     |
| German                     | Norwegian                  | Uzbek                      |
| Greek                      | Odia                       | Vietnamese                 |
| Gujarati                   | Yiddish                    | Welsh                      |
| Xhosa                      | Yoruba                     | Zulu                       |




# REDCap Language Library Translator

## How It Works

### User Input:
- The script prompts the user to select the JSON file using a graphical file dialog.
- The user specifies the target language for translation.

### Extract Default Values:
- The script extracts all "default" and "translation" values from the JSON file.

### Create Subfolder:
- A subfolder is created based on the version of the JSON file and the target language.

### Save Extracted Data:
- The extracted data is saved into a new JSON file within the subfolder.

### Translate Values:
- The script translates the "default" values in the new JSON file.
- If any translation errors occur, the corresponding key-value pairs are logged into a separate "errors" file.

### Update Original JSON:
- The script updates the original JSON file with the new translated values.
- The display and key fields are updated to reflect the new language.

### Cleanup:
- The temporary translation file is deleted.


## Usage
Command Line
After installing the package, you can use the command line tool redcap_translate to translate your JSON files:

```sh
redcap_translate
```

You will be prompted to select the JSON file and enter the language to translate the variables to.

### Error Handling
If any errors occur during the translation process, the script logs the corresponding key-value pairs into a separate file named {language}_Error.log within the subfolder. This allows users to review and address translation issues separately.

### Contributions
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue on GitHub.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgments
The googletrans package for providing translation capabilities.
The REDCap community for their support and resources.