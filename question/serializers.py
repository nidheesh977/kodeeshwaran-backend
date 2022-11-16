from rest_framework import serializers
from .models import Question, Option


class OptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Option
    fields = ["option","question","answer", "question_id"]

class QuestionSerializer(serializers.ModelSerializer):
  option = OptionSerializer(many = True)
  class Meta:
    model = Question
    fields = ["question", "question_no", "option"]
