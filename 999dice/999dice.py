import marshal,zlib,base64
exec(base64.b64decode("aW1wb3J0IHJlcXVlc3RzLGpzb24sdGltZSxzeXMscmFuZG9tLG9zLGFyZ3BhcnNlCmltcG9ydCBjb2xvcmFtYQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLCBCYWNrLCBTdHlsZQpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludApmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZQpjb2xvcmFtYS5pbml0KGF1dG9yZXNldD1UcnVlKQoKCgpwYXJzZXIgPSBhcmdwYXJzZS5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbj0nOTk5IERpY2UgQm90IHwgVGhpcyBJcyBHYW1ibGluZyBCb3QgUGxhc2UgVGFrZSBPd24gWW91ciBSaXNrJykKcGFyc2VyLmFkZF9hcmd1bWVudCgKICAgICctYycsJy0tYmV0c2V0JywKICAgIGRlZmF1bHQ9MCwKICAgIGhlbHA9J0VudGVyIFlvdXIgQmV0c2V0IE51bWJlciAoZGVmYXVsdDogMCknCikKbXlfbmFtZXNwYWNlID0gcGFyc2VyLnBhcnNlX2FyZ3MoKQoKCgoKCndpdGggb3BlbignY29uZmlnLmpzb24nLCAncicpIGFzIG15ZmlsZToKICAgICAgZGF0YT1teWZpbGUucmVhZCgpCiMgcGFyc2UgZmlsZQpvYmogPSBqc29uLmxvYWRzKGRhdGEpCgoKcHJpbnQgKFN0eWxlLk5PUk1BTCtGb3JlLk1BR0VOVEErIlxudC5tZS91YmlpZFxuIitTdHlsZS5OT1JNQUwrRm9yZS5HUkVFTisiXG49PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIkF1dGhvciBCeSAgIitTdHlsZS5ESU0rRm9yZS5XSElURSsiOiAiK1N0eWxlLlJFU0VUX0FMTCsiSU1TS0FBXG4iK1N0eWxlLkJSSUdIVCtGb3JlLkdSRUVOKyJDaGFubmVsIFl0ICIrU3R5bGUuTk9STUFMK0ZvcmUuV0hJVEUrIjoiK1N0eWxlLlJFU0VUX0FMTCsiIElNU0tBQSBaIitTdHlsZS5CUklHSFQrRm9yZS5HUkVFTisiXG45OTkgRGljZSBCb3QiK1N0eWxlLk5PUk1BTCtGb3JlLldISVRFKyIgfCAiK1N0eWxlLkJSSUdIVCtGb3JlLlJFRCsiTG9zZSBTdHJlYWsgIitTdHlsZS5OT1JNQUwrRm9yZS5XSElURSsifCIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIiBXaW4gU3RyZWFrXG4iK1N0eWxlLkJSSUdIVCtGb3JlLkdSRUVOKyJzdXBwb3J0IGJ5IGh0dHBzOi8vZ2l0aHViLmNvbS9Nb25rZXlELWNvcmUvOTk5XG4iK1N0eWxlLkJSSUdIVCtGb3JlLkdSRUVOKyJEb25hdGUgIitTdHlsZS5OT1JNQUwrRm9yZS5XSElURSsiOiIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIiBCVEMgIitTdHlsZS5SRVNFVF9BTEwrIjFGZzhZR0xXZ3g5anFWRUpkbUZwZXlzZWZadmdGOXdudEZcbiIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIiAgICAgICAgIExUQyAiK1N0eWxlLlJFU0VUX0FMTCsiTGZuR283N25oRTNOdEVCeTJVR0s2MWMzVGUxSjlIUWF2UFxuIitTdHlsZS5CUklHSFQrRm9yZS5HUkVFTisiICAgICAgICAgRG9nZSAiK1N0eWxlLlJFU0VUX0FMTCsiRDh0WUJSazNncVlpRlU0eGJkUG11elBjTmFuMzlaQjUzY1xuXG4iKQoKaGlqYXUgPSBTdHlsZS5CUklHSFQrRm9yZS5HUkVFTgoKcmVzID0gU3R5bGUuUkVTRVRfQUxMCmFidTIgPSBTdHlsZS5OT1JNQUwrRm9yZS5XSElURQp1bmd1ID0gU3R5bGUuTk9STUFMK0ZvcmUuTUFHRU5UQQpoaWphdTIgPSBTdHlsZS5OT1JNQUwrRm9yZS5HUkVFTgpyZWQyID0gU3R5bGUuTk9STUFMK0ZvcmUuUkVECnJlZCA9IFN0eWxlLkJSSUdIVCtGb3JlLlJFRApjID0gcmVxdWVzdHMuc2Vzc2lvbigpCgp1cmwgPSAiaHR0cHM6Ly93d3cuOTk5ZG9nZS5jb20vYXBpL3dlYi5hc3B4Igp1YSA9IHsKICJPcmlnaW4iOiAiZmlsZTovLyIsCiAidXNlci1hZ2VudCI6IG9ialsiVXNlci1BZ2VudCJdLAogIkNvbnRlbnQtdHlwZSI6ICJhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQiLAogIkFjY2VwdCI6ICIqLyoiLAogIkFjY2VwdC1MYW5ndWFnZSI6ICJpZC1JRCxpZDtxPTAuOSxlbi1VUztxPTAuOCxlbjtxPTAuNyIsCiAiWC1SZXF1ZXN0ZWQtV2l0aCI6ICJjb20ucmVsYW5kLnJlbGFuZGljZWJvdCIKfQoKZGVmIGtvbnZlcnQocGVyc2VuLHRhcnVoYW4pOgogICAgZ2xvYmFsIGhpZ2gKICAgIGdsb2JhbCBsb3cKICAgIGMgPSBzdHIoOTk5OTk5ICogZmxvYXQocGVyc2VuKSAvIDEwMCkKICAgIGlmIHRhcnVoYW4gPT0gIkhpIiBvciB0YXJ1aGFuID09ICJoaSIgb3IgdGFydWhhbiA9PSAiSEkiOgogICAgICAgbiA9IHN0cihjLnNwbGl0KCIuIilbMV0pCiAgICAgICBwYW5na2F0ID0gNiAtIGxlbihuKQogICAgICAgbG93ID0gaW50KGludChuKSAqICgxMCAqKiBwYW5na2F0KSkKICAgICAgIGhpZ2ggPSA5OTk5OTkKICAgIGlmIHRhcnVoYW4gPT0gIkxvIiBvciB0YXJ1aGFuID09ICJMT1ciIG9yIHRhcnVoYW4gPT0gImxvdyIgb3IgdGFydWhhbiA9PSAiTG93IiBvciB0YXJ1aGFuID09ICJMTyI6CiAgICAgICBsb3cgPSAwCiAgICAgICBoaWdoID0gaW50KGMuc3BsaXQoIi4iKVswXSkKCgpkZWYgcmV2KG51bSk6CiAgICBpZiAobGVuKG51bSkgPCA4KToKICAgICAgICBwYW5qYW5nX25vbCA9IGludCg4IC0gbGVuKG51bSkpCiAgICAgICAgbnVtID0gKChwYW5qYW5nX25vbCoiMCIpK3N0cihudW0pKQogICAgICAgIHJlc3VsdCA9ICgiMC4iK251bSkKICAgIGlmIChsZW4obnVtKSA9PSA4KToKICAgICAgICBwYW5qYW5nX25vbCA9IGludCg4IC0gbGVuKG51bSkpCiAgICAgICAgbnVtID0gKChwYW5qYW5nX25vbCoiMCIpK3N0cihudW0pKQogICAgICAgIHJlc3VsdCA9ICgiMC4iK251bSkKICAgIGVsc2U6CiAgICAgICAgbGVuX251bSA9IGxlbihudW0pCiAgICAgICAgZW5kID0gbnVtWy04Ol0KICAgICAgICBmaXJzdCA9IG51bVs6bGVuX251bS04XQogICAgICAgIHJlc3VsdCA9IChmaXJzdCsiLiIrZW5kKQogICAgcmV0dXJuIChyZXN1bHQpCgoKCmRlZiBkaWNlKHdzLGxzKToKICAgaWYgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiQXV0byIgb3IgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiYXV0byIgb3IgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiQVVUTyI6CiAgICAgIHVydXQgPSAwCiAgICAgIGp1bWxhaHVsYW5nPSAwCiAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgIGp1bWxhaHVsYW5nKz0xCiAgICAgICAgIHRyeToKICAgICAgICAgICAgIHBlc2FuID0gb2JqWyJDb25maWciXVtqdW1sYWh1bGFuZ11bIk5hbWUgQmV0IFNldCJdCiAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgIGJyZWFrCiAgIGVsc2U6CiAgICAgIHVydXQgPSBpbnQobXlfbmFtZXNwYWNlLmJldHNldCkKCiAgIHNscCA9IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJJbnRlcnZhbCJdKSAvIDEwMDAKICAgbGltaXRfYSA9IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJSZXNldCBJZiBXaW4iXSkgLSAxCiAgIHBheWluID0gaW50KGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkJhc2UgQmV0Il0pKigxMCAqKiA4KSkKICAga29udmVydChvYmpbIkNvbmZpZyJdW3VydXRdWyJDaGFuY2UiXSxvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiQmV0Il0pCiAgIGFtb3VudCA9IHBheWluCiAgIGRhdGEgPSB7CiAgICAgICJhIjogIlBsYWNlQmV0IiwKICAgICAgInMiOiBqc1siU2Vzc2lvbkNvb2tpZSJdLAogICAgICAiUGF5SW4iOiBhbW91bnQsCiAgICAgICJMb3ciOiBsb3csCiAgICAgICJIaWdoIjogaGlnaCwKICAgICAgIkNsaWVudFNlZWQiOiByYW5kaW50KDAsOTk5OTk5KSwKICAgICAgIkN1cnJlbmN5IjogImRvZ2UiLAogICAgICAiUHJvdG9jb2xWZXJzaW9uIjogIjIiCiAgIH0KICAgdHJ5OgogICAgIHIxID0gYy5wb3N0KHVybCxoZWFkZXJzPXVhLGRhdGE9ZGF0YSkKICAgICBqc24gPSBqc29uLmxvYWRzKHIxLnRleHQpCiAgICAganVtYmwgPSBqc25bIlN0YXJ0aW5nQmFsYW5jZSJdICsgaW50KGpzblsiUGF5T3V0Il0pIC0gaW50KGFtb3VudCkKICAgICBqdW0gPSBpbnQoanNuWyJQYXlPdXQiXSkgLSBpbnQoYW1vdW50KQogICAgIHByb2YgPSAoZmxvYXQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSArIGludChqc25bIlBheU91dCJdKSAtIGludChhbW91bnQpIC0ganVtYmwpLygxMCAqKiA4KSkKICAgICBwcmludCAoaGlqYXUrIlxuXG5cblN0YXJ0aW5nIEJhbGFuY2UiLHJlcytzdHIoKGZsb2F0KGludChqc25bIlN0YXJ0aW5nQmFsYW5jZSJdKSArIGludChqdW0pKS8oMTAgKiogOCkpKSkKICAgICBwcmludCAoIkFuZGEgTWVuZ2d1bmFrYW4gQmV0U2V0IEtlICIrb2JqWyJDb25maWciXVt1cnV0XVsiTmFtZSBCZXQgU2V0Il0pCiAgICAgbiA9IDAKICAgICBidXJzdCA9IEZhbHNlCiAgICAgc3RhdHNfcm9sZWJldF9sb3NlID0gRmFsc2UKICAgICBzdGF0c19yb2xlYmV0X3dpbiA9IEZhbHNlCiAgICAgbWVuaXQgPSBkYXRldGltZS5ub3coKS5zdHJmdGltZSgnJU0nKQogICAgIG1lbml0ID0gaW50KG1lbml0KSArIGludChvYmpbIkludGVydmFsIl0pCiAgICAgbm9fd2luID0gMAogICAgIG5vX2xvc2UgPSAwCiAgICAgdG90YWxfd2luPTAKICAgICB0b3RhbF9sb3NlPTAKICAgICBub19yb2xlYmV0ID0gMAogICAgIHJvbGViZXQ9IkhpIgogICAgIHJlc2V0X2lmX3Byb2ZpdCA9IG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJlc2V0IElmIFByb2ZpdCJdCiAgICAgdG90X2lmX3Byb2ZpdCA9IG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJlc2V0IElmIFByb2ZpdCJdCiAgICAgd2hpbGUgVHJ1ZToKICAgICAgICBpZiByZXNldF9pZl9wcm9maXQgPT0gIk9GRiIgb3IgcmVzZXRfaWZfcHJvZml0ID09ICJPZmYiIG9yIHJlc2V0X2lmX3Byb2ZpdCA9PSAib2ZmIjoKICAgICAgICAgICBzdGF0c19pZl9wcm9maXQgPSBGYWxzZQogICAgICAgIGVsc2U6CiAgICAgICAgICAgc3RhdHNfaWZfcHJvZml0ID0gVHJ1ZQogICAgICAgIGlmIG9ialsiQ29uZmlnIl1bdXJ1dF1bIk1heCBCZXQiXSA9PSAiT0ZGIiBvciBvYmpbIkNvbmZpZyJdW3VydXRdWyJNYXggQmV0Il0gPT0gIm9mZiIgb3Igb2JqWyJDb25maWciXVt1cnV0XVsiTWF4IEJldCJdID09ICJPZmYiOgogICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKCIiKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgaWYgYW1vdW50ID4gaW50KGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIk1heCBCZXQiXSkqKDEwICoqIDgpKToKICAgICAgICAgICAgICAgYW1vdW50ID0gcGF5aW4KICAgICAgICBpZiBvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiVG9nZ2xlIl0gPT0gIk9uIiBvciBvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiVG9nZ2xlIl0gPT0gIk9OIiBvciBvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiVG9nZ2xlIl0gPT0gIm9uIjoKICAgICAgICAgICAgbm9fcm9sZWJldCArPTEKICAgICAgICAgICAgaWYgc3RhdHNfcm9sZWJldF93aW4gaXMgVHJ1ZToKICAgICAgICAgICAgICAgaWYgbm9fcm9sZWJldCA+IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiSWYgV2luIl0pIC0gMToKICAgICAgICAgICAgICAgICAgcm9sZWJldCA9ICJMbyIKICAgICAgICAgICAgICAgaWYgbm9fcm9sZWJldCA+IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiSWYgV2luIl0pICogMiAtIDE6CiAgICAgICAgICAgICAgICAgIHJvbGViZXQgPSAiSGkiCiAgICAgICAgICAgICAgICAgIG5vX3JvbGViZXQgPSAwCiAgICAgICAgICAgIGlmIHN0YXRzX3JvbGViZXRfbG9zZSBpcyBUcnVlOgogICAgICAgICAgICAgICBpZiBub19yb2xlYmV0ID4gaW50KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkJldCJdWyJIaSAvIExvdyJdWyJJZiBMb3NlIl0pIC0xIDoKICAgICAgICAgICAgICAgICAgcm9sZWJldCA9ICJMbyIKICAgICAgICAgICAgICAgaWYgbm9fcm9sZWJldCA+IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiSWYgTG9zZSJdKSAqIDIgLSAxOgogICAgICAgICAgICAgICAgICByb2xlYmV0ID0gIkhpIgogICAgICAgICAgICAgICAgICBub19yb2xlYmV0ID0gMAogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHJvbGViZXQgPSBvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiQmV0Il0KICAgICAgICBpZiBteV9uYW1lc3BhY2UuYmV0c2V0ID09ICJBdXRvIiBvciBteV9uYW1lc3BhY2UuYmV0c2V0ID09ICJBVVRPIiBvciBteV9uYW1lc3BhY2UuYmV0c2V0ID09ICJhdXRvIjoKICAgICAgICAgIHdha3R1ID0gZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoJyVNJykKICAgICAgICAgIGlmIGludCh3YWt0dSkgPiBpbnQobWVuaXQgLSAxKToKICAgICAgICAgICAgIG1lbml0ID0gaW50KG1lbml0KSArIGludChvYmpbIkludGVydmFsIl0pCiAgICAgICAgICAgICB1cnV0ICs9MQogICAgICAgICAgICAgaWYgdXJ1dCA9PSBqdW1sYWh1bGFuZzoKICAgICAgICAgICAgICAgIHVydXQgPSAwCiAgICAgICAgICAgICBwcmludCAoIkNoYW5nZSBCZXQgU2V0ICIrb2JqWyJDb25maWciXVt1cnV0XVsiTmFtZSBCZXQgU2V0Il0rIiAgICAgICAgICAgICAgICAgICAgICAgICAgICIpCiAgICAgICAgICAgICBzbHAgPSBpbnQob2JqWyJDb25maWciXVt1cnV0XVsiSW50ZXJ2YWwiXSkgLyAxMDAwCiAgICAgICAgICAgICBsaW1pdF9hID0gaW50KG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJlc2V0IElmIFdpbiJdKSAtIDEKICAgICAgICAgICAgIHBheWluID0gaW50KGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkJhc2UgQmV0Il0pKigxMCAqKiA4KSkKICAgICAgICAgICAgIGFtb3VudCA9IHBheWluCgogICAgICAgIGVsc2U6CiAgICAgICAgICB1cnV0ID0gaW50KG15X25hbWVzcGFjZS5iZXRzZXQpCgogICAgICAgIGlmIG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJhbmRvbSBDaGFuY2UiXVsiVG9nZ2xlIl0gPT0gIk9OIiBvciBvYmpbIkNvbmZpZyJdW3VydXRdWyJSYW5kb20gQ2hhbmNlIl1bIlRvZ2dsZSJdID09ICJPbiIgb3Igb2JqWyJDb25maWciXVt1cnV0XVsiUmFuZG9tIENoYW5jZSJdWyJUb2dnbGUiXSA9PSAib24iOgogICAgICAgICAgIGhhc2lsX2NoYW5jZSA9IHJvdW5kKHJhbmRvbS51bmlmb3JtKGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJhbmRvbSBDaGFuY2UiXVsiTWluIl0pLGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJhbmRvbSBDaGFuY2UiXVsiTWF4Il0pKSwyKQogICAgICAgICAgIGNvayA9IGxlbihzdHIoaGFzaWxfY2hhbmNlKSkKICAgICAgICAgICBpZiBjb2sgPT0gMzoKICAgICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKCJcciIrc3RyKGhhc2lsX2NoYW5jZSkrIiAgICIpCiAgICAgICAgICAgaWYgY29rID09IDQ6CiAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHIiK3N0cihoYXNpbF9jaGFuY2UpKyIgICIpCiAgICAgICAgICAgaWYgY29rID09IDU6CiAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHIiK3N0cihoYXNpbF9jaGFuY2UpKyIgIikKICAgICAgICAgICBrb252ZXJ0KGhhc2lsX2NoYW5jZSxzdHIocm9sZWJldCkpCiAgICAgICAgZWxzZToKICAgICAgICAgICBrb252ZXJ0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkNoYW5jZSJdLHN0cihyb2xlYmV0KSkKCiAgICAgICAgdGltZS5zbGVlcChmbG9hdChzbHApKQogICAgICAgIGFtb3VudCA9IGludChhbW91bnQpCiAgICAgICAgbis9MQogICAgICAgIGRhdGEgPSB7CiAgICAgICAgICAiYSI6ICJQbGFjZUJldCIsCiAgICAgICAgICAicyI6IGpzWyJTZXNzaW9uQ29va2llIl0sCiAgICAgICAgICAiUGF5SW4iOiBhbW91bnQsCiAgICAgICAgICAiTG93IjogbG93LAogICAgICAgICAgIkhpZ2giOiBoaWdoLAogICAgICAgICAgIkNsaWVudFNlZWQiOiByYW5kaW50KDAsOTk5OTk5KSwKICAgICAgICAgICJDdXJyZW5jeSI6ICJkb2dlIiwKICAgICAgICAgICJQcm90b2NvbFZlcnNpb24iOiAiMiIKICAgICAgICB9CiAgICAgICAgaWYgcHJvZiA+IGZsb2F0KG9ialsiVGFyZ2V0IFByb2ZpdCJdKToKICAgICAgICAgICBwcmludCAoaGlqYXUrIlxuWWF5LiEgXG5Qcm9maXQgTWVuY2FwYWkgVGFyZ2V0Li4uLi4hXG4iK2hpamF1KyJQcm9maXQgIityZXMrc3RyKHByb2YpKQogICAgICAgICAgIG9zLnN5c3RlbSgidGVybXV4LXRvYXN0IFlvdSB3aW4gIitzdHIocHJvZikpCiAgICAgICAgICAgdGltZS5zbGVlcCgxKQogICAgICAgICAgIG9zLnN5c3RlbSgidGVybXV4LXRvYXN0IFRvdGFsIEJhbGFuY2UgIitzdHIoZmxvYXQoaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkpLygxMCAqKiA4KSkpCiAgICAgICAgICAgc3lzLmV4aXQoKQogICAgICAgIHIxID0gYy5wb3N0KHVybCxoZWFkZXJzPXVhLGRhdGE9ZGF0YSkKICAgICAgICBqc24gPSBqc29uLmxvYWRzKHIxLnRleHQpCiAgICAgICAgcHJvZiA9IChmbG9hdChqc25bIlN0YXJ0aW5nQmFsYW5jZSJdICsgaW50KGpzblsiUGF5T3V0Il0pIC0gaW50KGFtb3VudCkgLSBqdW1ibCkvKDEwICoqIDgpKQogICAgICAgIGp1bSA9IGludChqc25bIlBheU91dCJdKSAtIGludChhbW91bnQpCiAgICAgICAgaWYganNuWyJTdGFydGluZ0JhbGFuY2UiXSA+IHdzOgogICAgICAgICAgIHByaW50ICh1bmd1KyJbIityZXMrc3RyKHJvbGViZXQpK3VuZ3UrIl0gIitoaWphdTIrc3RyKGZsb2F0KGFtb3VudCkvKDEwICoqIDgpKSxyZXMrc3RyKGZsb2F0KGludChqc25bIlN0YXJ0aW5nQmFsYW5jZSJdKSArIGludChqdW0pKS8oMTAgKiogOCkpLGhpamF1MisiUHJvZml0IixyZXMrc3RyKHByb2YpKQogICAgICAgICAgIHByaW50IChoaWphdSsiWWF5LiFcbkJhbGFuY2UgU3VkYWggTWVtZW51aGkgVGFyZ2V0Li4uLi4hIikKICAgICAgICAgICBvcy5zeXN0ZW0oInRlcm11eC10b2FzdCBUYXJnZXQgV2luIFN1ZGFoIFRlcmNhcGFpIikKICAgICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICAgICAgICAgb3Muc3lzdGVtKCJ0ZXJtdXgtdG9hc3QgVG90YWwgQmFsYW5jZSAiK3N0cihmbG9hdChpbnQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSkgKyBpbnQoanVtKSkvKDEwICoqIDgpKSkKICAgICAgICAgICBzeXMuZXhpdCgpCiAgICAgICAgaWYganNuWyJTdGFydGluZ0JhbGFuY2UiXSA8IGxzOgogICAgICAgICAgIHByaW50ICh1bmd1KyJbIityZXMrc3RyKHJvbGViZXQpK3VuZ3UrIl0iK3JlZDIrIi0iK3N0cihmbG9hdChhbW91bnQpLygxMCAqKiA4KSkscmVzK3N0cigoZmxvYXQoaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkpLygxMCAqKiA4KSkpLHJlZDIrIkxvc2UgIixyZXMrc3RyKHByb2YpKQogICAgICAgICAgIHByaW50IChTdHlsZS5CUklHSFQrRm9yZS5SRUQrIkxvc2UgVGFyZ2V0Li4uLiEiKQogICAgICAgICAgIG9zLnN5c3RlbSgidGVybXV4LXRvYXN0IExvc2UgVGFyZ2V0ICIpCiAgICAgICAgICAgdGltZS5zbGVlcCgxKQogICAgICAgICAgIG9zLnN5c3RlbSgidGVybXV4LXRvYXN0IFRvdGFsIEJhbGFuY2UgIitzdHIoZmxvYXQoaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkpLygxMCAqKiA4KSkpCiAgICAgICAgICAgc3lzLmV4aXQoKQogICAgICAgIGlmIGpzblsiUGF5T3V0Il0gaXMgbm90IDA6CiAgICAgICAgICAgbm9fd2luICs9MQogICAgICAgICAgIG5vX2xvc2UgPSAwCiAgICAgICAgICAgYmFsID0gaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkKICAgICAgICAgICBpZiBwcm9mID4gMDoKICAgICAgICAgICAgIHByaW50ICh1bmd1KyJbIityZXMrc3RyKHJvbGViZXQpK3VuZ3UrIl0gIitoaWphdTIrc3RyKHJldihzdHIoYW1vdW50KSkpLHJlcytzdHIocmV2KHN0cihiYWwpKSksaGlqYXUyKyJQcm9maXQiLHJlcytzdHIocHJvZikpCiAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgIHByaW50ICh1bmd1KyJbIityZXMrc3RyKHJvbGViZXQpK3VuZ3UrIl0gIitoaWphdTIrc3RyKHJldihzdHIoYW1vdW50KSkpLHJlcytzdHIocmV2KHN0cihiYWwpKSkscmVkMisiTG9zZSAiLHJlcytzdHIocHJvZikpCiAgICAgICAgICAgYW1vdW50ID0gaW50KGFtb3VudCkgKiBmbG9hdChvYmpbIkNvbmZpZyJdW3VydXRdWyJJZiBXaW4iXSkKCiAgICAgICAgZWxzZToKICAgICAgICAgICBub193aW4gPSAwCiAgICAgICAgICAgbm9fbG9zZSArPTEKICAgICAgICAgICBpID0gMAogICAgICAgICAgIGJ1cnN0ID0gVHJ1ZQogICAgICAgICAgIGJhbCA9IGludChqc25bIlN0YXJ0aW5nQmFsYW5jZSJdKSArIGludChqdW0pCiAgICAgICAgICAgaWYgcHJvZiA+IDA6CiAgICAgICAgICAgICBwcmludCAodW5ndSsiWyIrcmVzK3N0cihyb2xlYmV0KSt1bmd1KyJdIityZWQyKyItIitzdHIocmV2KHN0cihhbW91bnQpKSkscmVzK3N0cihyZXYoc3RyKGJhbCkpKSxoaWphdTIrIlByb2ZpdCIscmVzK3N0cihwcm9mKSkKICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgcHJpbnQgKHVuZ3UrIlsiK3JlcytzdHIocm9sZWJldCkrdW5ndSsiXSIrcmVkMisiLSIrc3RyKHJldihzdHIoYW1vdW50KSkpLHJlcytzdHIocmV2KHN0cihiYWwpKSkscmVkMisiTG9zZSAiLHJlcytzdHIocHJvZikpCiAgICAgICAgICAgYW1vdW50ID0gaW50KGFtb3VudCkgKiBmbG9hdChvYmpbIkNvbmZpZyJdW3VydXRdWyJJZiBMb3NlIl0pCiAgICAgICAgaWYgc3RhdHNfaWZfcHJvZml0IGlzIFRydWU6CiAgICAgICAgICAgIGlmIHByb2YgPiBmbG9hdChyZXNldF9pZl9wcm9maXQpOgogICAgICAgICAgICAgICBhbW91bnQgPSBwYXlpbgogICAgICAgICAgICAgICByZXNldF9pZl9wcm9maXQgPSBmbG9hdChwcm9mKStmbG9hdCh0b3RfaWZfcHJvZml0KQoKICAgICAgICBpZiBidXJzdCBpcyBUcnVlOgogICAgICAgICAgIGkrPTEKICAgICAgICAgICBpZiBpID4gbGltaXRfYToKICAgICAgICAgICAgIGkgPSAwCiAgICAgICAgICAgICBidXJzdCA9IEZhbHNlCiAgICAgICAgZWxzZToKICAgICAgICAgICBpZiBuID4gbGltaXRfYToKICAgICAgICAgICAgIG4gPSAwCiAgICAgICAgICAgICBhbW91bnQgPSBwYXlpbgoKICAgICAgICBpZiBub193aW4gPiB0b3RhbF93aW46CiAgICAgICAgICAgc3RhdHNfcm9sZWJldF93aW4gPSBUcnVlCiAgICAgICAgICAgc3RhdHNfcm9sZWJldF9sb3NlID0gRmFsc2UKICAgICAgICAgICB0b3RhbF93aW4gKz0xCiAgICAgICAgaWYgbm9fbG9zZSA+IHRvdGFsX2xvc2U6CiAgICAgICAgICAgc3RhdHNfcm9sZWJldF9sb3NlID0gVHJ1ZQogICAgICAgICAgIHN0YXRzX3JvbGViZXRfd2luID0gRmFsc2UKICAgICAgICAgICB0b3RhbF9sb3NlICs9MQogICAgICAgIHN5cy5zdGRvdXQud3JpdGUoaGlqYXUrIiAgICAgICAgV2luIFN0cmVhayAiK3JlcytzdHIodG90YWxfd2luKStyZWQrIiBMb3NlIFN0cmVhayAiK3JlcytzdHIodG90YWxfbG9zZSkrIlxyIikKICAgICAgICBpZiBvYmpbIkF1dG8gV2QiXVsiVG9nZ2xlIl0gPT0gIk9uIiBvciBvYmpbIkF1dG8gV2QiXVsiVG9nZ2xlIl0gPT0gIk9OIiBvciBvYmpbIkF1dG8gV2QiXVsiVG9nZ2xlIl0gPT0gIm9uIjoKICAgICAgICAgICBpZiBmbG9hdChyZXYoc3RyKGJhbCkpKSA+IGZsb2F0KG9ialsiQXV0byBXZCJdWyJJZiBCYWxhbmNlIl0pOgogICAgICAgICAgICAgIHdkID0gewogICAgICAgICAgICAgICAgImEiOiAiV2l0aGRyYXciLAogICAgICAgICAgICAgICAgInMiOiBqc1siU2Vzc2lvbkNvb2tpZSJdLAogICAgICAgICAgICAgICAgIkFtb3VudCI6IGludChmbG9hdChvYmpbIkF1dG8gV2QiXVsiQW1vdW50Il0pKigxMCAqKiA4KSksCiAgICAgICAgICAgICAgICAiQWRkcmVzcyI6IG9ialsiQXV0byBXZCJdWyJXYWxsZXQgQWRkcmVzcyJdLAogICAgICAgICAgICAgICAgIlRvdHAiOiAiIiwKICAgICAgICAgICAgICAgICJDdXJyZW5jeSI6ICJkb2dlIgoKICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgcjEgPSBjLnBvc3QodXJsLGhlYWRlcnM9dWEsZGF0YT13ZCkKICAgICAgICAgICAgICB3aXRoZHJhdyA9IGpzb24ubG9hZHMocjEudGV4dCkKICAgICAgICAgICAgICBwcmludCAoIiIpCiAgICAgICAgICAgICAgcHJpbnQgKCJXaXRoZHJhdyAiK3N0cihyZXYoc3RyKHdpdGhkcmF3WyJQZW5kaW5nIl0pKSkpCiAgICAgICAgICAgICAgd2l0aCBvcGVuKCJoaXN0b3J5LmxvZyIsImErIikgYXMgZjoKICAgICAgICAgICAgICAgICAgZi53cml0ZSgiV2l0aGRyYXcgIitzdHIocmV2KHN0cih3aXRoZHJhd1siUGVuZGluZyJdKSkpKyJcbiIpCiAgICAgICAgICAgICAgc3lzLmV4aXQoKQoKCgogICBleGNlcHQ6CiAgICAgICBwcmludCAoIiIpCiAgICAgICBvcy5zeXN0ZW0oInRlcm11eC10b2FzdCBCZXR0aW5nIFN0b3AiKQogICAgICAgdHJ5OgogICAgICAgICAgd2l0aCBvcGVuKCJoaXN0b3J5LmxvZyIsImErIikgYXMgZjoKICAgICAgICAgICAgICBmLndyaXRlKCJbIitkYXRldGltZS5ub3coKS5zdHJmdGltZSgnJVkvJW0vJWQgJUg6JU06JVMnKSsiXSBXaW4gU3RyZWFrICIrc3RyKHRvdGFsX3dpbikrIiBMb3NlIFN0cmVhayAiK3N0cih0b3RhbF9sb3NlKSsiIHwgQmFsYW5jZSAiK3N0cihmbG9hdChpbnQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSkgKyBpbnQoanVtKSkvKDEwICoqIDgpKSsiIFByb2ZpdCAiK3N0cihwcm9mKSsiXG4iKQogICAgICAgZXhjZXB0OgogICAgICAgICAgcHJpbnQgKHJlZDIrIkJhbGFuY2UgTm90IEVub3VnaCIpCiAgICAgICBzeXMuZXhpdCgpCnIgPSBjLmdldCh1cmwsaGVhZGVycz11YSxkYXRhPXsiYSI6ICJMb2dpbiIsIktleSI6ICI3ZWM3ZjhhMmM5NzI0YjJjYmI4ZWQ3NWU3MmI0N2VlOSIsIlVzZXJuYW1lIjogb2JqWyJBY2NvdW50Il1bIlVzZXJuYW1lIl0sIlBhc3N3b3JkIjogb2JqWyJBY2NvdW50Il1bIlBhc3N3b3JkIl0sIlRvdHAiOiAiIn0pCmpzID0ganNvbi5sb2FkcyhyLnRleHQpCnRyeToKICBwcmludCAoaGlqYXUrIkJhbGFuY2UgIithYnUyKyI6ICIrcmVzK3N0cihmbG9hdChqc1siRG9nZSJdWyJCYWxhbmNlIl0pLygxMCAqKiA4KSkpCmV4Y2VwdDoKICBwcmludCAoIkNoZWNrIFlvdXIgVXNlcm5hbWUgQW5kIFlvdXIgUGFzc3dvcmQiKQogIHN5cy5leGl0KCkKCgpkaWNlKGludChmbG9hdChvYmpbIlRhcmdldCBXaW4iXSkqKDEwICoqIDgpKSxpbnQoZmxvYXQob2JqWyJMb3NlIFRhcmdldCJdKSooMTAgKiogOCkpKQ=="))
