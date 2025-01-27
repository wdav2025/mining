# Two functions for querying the JSON endpoint of api.reporter.nih.gov - one from the CLI and one from a file: payload.json
#
#  exmple use:
#     . querying_reporter.nih.gov.sh      #  . means source, which loads this script into the shell environment so you can run from_file() or inline()
#     from_file
inline () {
curl -sX POST https://api.reporter.nih.gov/v2/projects/search \
  -H "Content-Type: application/json" \
  -d '{"key1":"value1", "key2":"value2"}'
}

from_file () {
curl -sX POST https://api.reporter.nih.gov/v2/projects/search \
  -H "Content-Type: application/json" \
  -d @payload.json
}
