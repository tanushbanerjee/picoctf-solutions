# Matryoshka Doll
- using binwalk, then extracting the image, using this command:
```bash
binwalk -e dolls.jpg
```
and then going to the extracted directory, then base_images, and extracting the image inside that directory again and then continue this process until you find the flag!, which is picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}
