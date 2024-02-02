# Takes in a list of dictionaries
# eg [{"trait_type":"1_TORSO","value":"TORSO_Myc-03-Petri-01.mov"}', '{"trait_type":"2_LEFTARM","value":"LEFTARM_Myc-12-BlackMold-02.mov"}']
# Extract the values from the list and append them to an empty list.
# Randomize a name, call the function "gen_api" with the list and name.
# Should return a wasabi bucket url.
@app.route('/api_generate', methods=['POST'])
def receive_data():
  try:
      data = request.get_json()
      selected_values = data.get('selectedValues', [])
  
      # Parse JSON strings and extract values
      list = []
      for json_string in selected_values:
          parsed_object = json.loads(json_string)
          list.append(parsed_object['value'])

      name = data.get('name', None)
      if name is None:
          name = ''.join(random.choices(string.ascii_letters, k=8))

      return jsonify({"generated_video": gen_api(list, name)})

  except Exception as e:
      return jsonify({"error": str(e)})
  

# Route that fetches existing files in project sub-directories  
# Set up to retrieve a "project" and "search_term" param - uses to return files 
@app.route('/get_files', methods=['GET'])
def get_files():
    project = request.args.get('project', '')
    search_term = request.args.get('search_term', '')
    folder_path = f'{project}/{search_term}'  # Adjust the path accordingly

    try:
      files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
      return jsonify({'files': files})
    except FileNotFoundError:
      return jsonify({'error': f'Folder not found: {folder_path}'})
    except Exception as e:
      return jsonify({'error': str(e)})
    

# 2 params - name, amount -> passes into "loop" function in "run_loop.py"
# If name is not provided - assign random name
# If amt is not provided - set to 1 
@app.route("/api_call", methods=['POST'])
def generate_mp4():
  data = request.get_json()

  name = data.get('name', None)
  if name is None:
      name = ''.join(random.choices(string.ascii_letters, k=8))

  amount = data.get('amount', None)
  if amount is None or not isinstance(amount, int) or amount <= 0:
      amount = 1

  try:
    final_url = loop(name, amount)
    return jsonify({"generated_video": final_url })
  except Exception as e:
    return jsonify({"Error": str(e)})