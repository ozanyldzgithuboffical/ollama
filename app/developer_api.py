# app.py

import json
from flask import Flask, jsonify, request

from app.helper.validator.simple_key_validator import SimpleKeyValidator
from service.config.ollama_settings import OllamaConfigurationEnum
from service.developer.developer_service import OllamaCodeSolving
from service.developer.reviewer_service import OllamaCodeReviewer
from service.developer.test_writer_service import OllamaTestWriter

app = Flask(__name__)


@app.route('/ollamadeveloperconfigsettings', methods=['GET'])
def solve_code():
    ollama_code_solver = OllamaCodeSolving()
    return jsonify(ollama_code_solver.get_default_config_settings())


@app.route('/ollamaaicodedeveloper', methods=['POST'])
def solve_code_dev():
    user_request = json.loads(request.data)
    if not SimpleKeyValidator.key_validation(user_request):
        return jsonify({'error': 'Invalid key error.'}), 400
    if OllamaConfigurationEnum.temperature in user_request.keys() and OllamaConfigurationEnum.num_ctx in user_request.keys():
        ollama_code_solver = OllamaCodeSolving(user_request["temperature"], user_request["num_ctx"])
    else:
        ollama_code_solver = OllamaCodeSolving()

    return jsonify(
        ollama_code_solver.general_code_solver(user_request["programmingLanguage"], user_request["userQuery"]))


@app.route('/ollamaaicodedeveloperadvanced', methods=['POST'])
def solve_code_dev_advanced():
    user_request = json.loads(request.data)
    if not SimpleKeyValidator.key_validation(user_request):
        return jsonify({'error': 'Invalid key error.'}), 400
    if OllamaConfigurationEnum.temperature in user_request.keys() and OllamaConfigurationEnum.num_ctx in user_request.keys():
        ollama_code_solver = OllamaCodeSolving(user_request["temperature"], user_request["num_ctx"])
    else:
        ollama_code_solver = OllamaCodeSolving()

    return jsonify(
        ollama_code_solver.general_code_solver(user_request["programmingLanguage"], user_request["userQuery"]))


@app.route('/ollamaaicodereviewer', methods=['POST'])
def review_dev_advanced():
    user_request = json.loads(request.data)
    if not SimpleKeyValidator.key_validation_reviewer(user_request):
        return jsonify({'error': 'Invalid key error.'}), 400
    if OllamaConfigurationEnum.temperature in user_request.keys() and OllamaConfigurationEnum.num_ctx in user_request.keys():
        ollama_code_reviewer = OllamaCodeReviewer(user_request["temperature"], user_request["num_ctx"])
    else:
        ollama_code_reviewer = OllamaCodeReviewer()

    return jsonify(
        ollama_code_reviewer.general_code_reviewer(user_request["pullRequestTitle"], user_request["userQuery"],
                                                   user_request["isVerbose"]))


@app.route('/ollamaaitestwriter', methods=['POST'])
def ai_tester_api():
    user_request = json.loads(request.data)
    if not SimpleKeyValidator.key_validation_tester(user_request):
        return jsonify({'error': 'Invalid key error.'}), 400
    if OllamaConfigurationEnum.temperature in user_request.keys() and OllamaConfigurationEnum.num_ctx in user_request.keys():
        ollama_test_writer = OllamaTestWriter(user_request["temperature"], user_request["num_ctx"])
    else:
        ollama_test_writer = OllamaTestWriter()

    return jsonify(
        ollama_test_writer.general_test_writer(user_request["userQuery"],
                                               user_request["instruction"],
                                               user_request["isVerbose"]))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
