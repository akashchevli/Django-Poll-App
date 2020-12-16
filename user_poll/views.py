from django.contrib.messages.api import success
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from user_poll.models import Questions, Answers, Voting
from django.contrib.auth.models import User


# Create your views here.
def add_poll(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        # Get the current logged in user id
        user = User.objects.get(id=request.POST['user_id'])

        # Store the data
        question = Questions(
            by_publishe = user,
            # Get text from the textbox
            question = request.POST['text']
        )
        # It will save the data into database
        question.save()

        # Get the current question id
        question_id = Questions.objects.get(question_id=question.question_id)

        # Store the choice1 data
        answer1 = Answers(
            question_id = question_id,
            answer = request.POST['choice1']
        )
        # Store the choice2 data
        answer2 = Answers(
            question_id = question_id,
            answer = request.POST['choice2']
        )
        # Save the data
        answer1.save()
        answer2.save()

        messages.success(request, 'New poll is added')
        return redirect('/')

    else:
        return render(request, 'polls/add_poll.html')

def poll_voting(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    # Question
    question = get_object_or_404(Questions, question_id=id)
    # Options of that question
    options = Answers.objects.filter(question_id = question)
    voting = Voting.objects.filter(question_id = question).count()
    print(voting)
    context = {
        'question': question,
        'options': options,
        'total_voting': voting
    }

    if request.method == 'POST':
        user = request.user
        choice = request.POST['option']
        answer = Answers.objects.get(answer=choice)
        if Voting.objects.filter(by_publishe = user, question_id = question, answer_id = answer).exists():
            messages.error(request, "You have already voted")
            return redirect('/')    
        if Voting.objects.filter(by_publishe = user, question_id = question).count() == 1:
            messages.error(request, "You have already voted")
            return redirect('/') 
    
        voting = Voting(by_publishe=user, question_id=question, answer_id=answer)
        voting.save()
        messages.success(request, 'Thank you for you vote')
        return redirect('/')

    return render(request, 'polls/poll_voting.html', context)
        

def edit_poll(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    question = Questions.objects.get(question_id = id)
    answer = Answers.objects.filter(question_id = question.question_id)
    total_option = len(answer)
    print(question)
    print(answer)
    if request.method == 'POST':    
        question = Questions.objects.filter(question_id = question.question_id).update(question = request.POST['text'])
        return redirect('/')

    context = {
        'question': question,
        'answer': answer,
        'total_option': total_option
    }
    return render(request, 'polls/edit_poll.html', context)

def edit_option(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    answer_id = Answers.objects.get(answer_id = id)

    context = {
        'answer_id': answer_id 
    }

    if request.method == 'POST':
        Answers.objects.filter(answer_id = answer_id.answer_id).update(answer = request.POST['text'])
        return redirect('/')
        
        
    return render(request, 'polls/edit_option.html', context)

def add_option(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    question = Questions.objects.get(question_id = id)
    context = {
        'question': question
    }
    if request.method == 'POST':
        add_option = Answers(question_id = question, answer = request.POST['add_option'])
        add_option.save()
        return redirect('edit_poll', id=question.question_id)
    
    return render(request, 'polls/add_option.html', context)

def delete_option(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    answer = Answers.objects.get(answer_id = id)
    print(answer.answer_id)
    question = Answers.objects.filter(answer_id = answer.answer_id).values('question_id')[0]['question_id']
    print(answer)
    print(question)
    answer.delete()
    return redirect('edit_poll', id=question)

def delete_poll(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    question = Questions.objects.get(question_id = id)
    question.delete()
    return redirect('/')   


def poll_stop(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    # return the question of the corrosponding id
    question = get_object_or_404(Questions, question_id = id)

    # give the total votes of the question
    voting = Voting.objects.filter(question_id = question).count()

    # return the options of the corresponding question
    options = Answers.objects.filter(question_id = question)
    
    # return the answer_id of the answer according to the vote given by user
    # if i not use .values function it will return below output.
    """ <QuerySet [<Voting: Hard work or Smart work?-Hard work or Smart work?-Smart work-akash>, 
        <Voting: Hard work or Smart work?-Hard work or Smart work?-Hard work-yash>,
        <Voting: Hard work or Smart work?-Hard work or Smart work?-Smart work-abhi>]> """
    counts = Voting.objects.filter(question_id = question.question_id).values('answer_id')

    # whatever we pass in .values function it will return that
    # <QuerySet [{'answer_id': 22}, {'answer_id': 21}, {'answer_id': 22}]>
 
    # Count the vote for each option
    # {22: 2, 21: 1}
    res = {}
    for i in counts:
        if i['answer_id'] in res: 
            res[i['answer_id']] += 1
        else:
            res[i['answer_id']] = 1
    
 
    res = dict(sorted(res.items()))
    res = res.values()
    aa = zip(options, res)
    
    voting_percentage = []
    for res in res:
        percentage = (res / voting) * 100
        voting_percentage.append("{:.2f}".format(percentage))
        
    if question.is_published is True:
        question.is_published = False
        print(question.is_published)
        question.save() 

    context = {
        'question': question,
        'voting': voting,
        'aa': aa,
        'res': res,
        'voting_percentage': voting_percentage
    }

    # if question.is_published is True:
    #is_published = question.values('is_published')
     
    #     return render(request, 'pages/index.html', context)
    return render(request, 'polls/poll_stop.html', context)