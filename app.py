from flask import Flask, render_template, request, redirect, url_for
import cohere
# import logging

# logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

co = cohere.Client('YOUR_API_KEY')   ## here I used Cohere api key 

topics = ["Geography", "Health", "Sports"]  
questions_answers = []  
correct_answer = ""
count = 0
selected_topic = "12345678"
@app.route('/', methods=['GET', 'POST'])
def home():
    global selected_topic
    if request.method == 'POST':
        selected_topic = request.form['topic']
        # print(selected_topic,"<-------------->")
        
        return redirect(url_for('index',topics=selected_topic))
    return render_template('home.html', topics=topics)

@app.route('/quiz', methods=['GET', 'POST'])
def index():
    global correct_answer
    global count
    global selected_topic
    
    if request.method == 'POST':
        if 'generate' in request.form:
            # selected_topic = request.args.get('topic', '')

            # topic = request.form['topic']
            prompt = f"Generate a random question on the topic of {selected_topic}."
            response = co.generate(
                model='command-xlarge-nightly',
                prompt=prompt,
                max_tokens=100
            )
            question = response.generations[0].text.strip()
            correct_answer_response = co.generate( 
                model='command-xlarge-nightly',
                prompt=question,  
                max_tokens=100
            )
            correct_answer = correct_answer_response.generations[0].text.strip() 

            questions_answers.append({"question": question, "topic": selected_topic})
            return render_template('index.html', topics=topics, question=question)
        elif 'evaluate' in request.form:
            question = request.form['question']
            
            answer = request.form['answer']

            prompt = f"Question: {question}\nUser_Answer: {answer}\nEvaluate the answer for correctness and relevance. the evaluation should not be more than 20 words"
            response = co.generate(
                model='command-xlarge-nightly',
                prompt=prompt,
                max_tokens=100
            )
            evaluation = response.generations[0].text.strip()
            # correct_answer = evaluation
            evaluation_of_answer = evaluate_answer(question, answer, correct_answer)
            # print(evaluation_of_answer,"---->-------<>")
            if evaluation_of_answer.lower() == "correct":
                    count += 1
            return render_template('index.html', topics=topics, question=question, answer=answer, evaluation=evaluation)
        elif 'end_test' in request.form:
            
            total_questions = len(questions_answers)
            correct_answers = 0
            # print(questions_answers)
            
            return render_template('result.html', total_questions=total_questions, correct_answers=count, questions_answers=questions_answers)
    return render_template('index.html', topics=topics)

def evaluate_answer(question, user_answer,correct_answer):
    prompt = f"Question: {question}\nUser's Answer: {user_answer}\nCorrect Answer: {correct_answer}\nEvaluate the user's answer for correctness and relevance and reply in one word only correct if users answer is correct and inccorect if users answer is incorrect."
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100
    )
    evaluation = response.generations[0].text.strip()
    # print(question,user_answer,"---",correct_answer,evaluation,"----->")

    return evaluation
if __name__ == '__main__':
    app.run(debug=True)
