{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled3.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPmWyVEZdG5gGThHaT5hsu1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tackulus/Finished-Course/blob/main/Untitled3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "id": "qHaPxEFBQjno",
        "outputId": "67e29c75-0082-480d-c192-e0955b8df0b9"
      },
      "source": [
        "import sys\n",
        "\n",
        "lines = []\n",
        "for line in sys.stdin:\n",
        "    lines.append(line.rstrip('\\n'))\n",
        "# key, answers = lines[0], lines[1:]\n",
        "\n",
        "def check_answer(key, ans):\n",
        "    score = 0\n",
        "    for i in range(len(key)):\n",
        "        if key[i] == ans[i]: score += 1\n",
        "    return score\n",
        "\n",
        "for ans in answers:\n",
        "    score = check_answer(key, line)\n",
        "    print(score)\n"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-23621ea4d9f9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     12\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mscore\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mans\u001b[0m \u001b[0;32min\u001b[0m \u001b[0manswers\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m     \u001b[0mscore\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcheck_answer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mline\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mscore\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'answers' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rwmmkuRtSORZ"
      },
      "source": [
        "L = [\"aaaaaaa\\n\",\n",
        "     \"agajkka\\n\",\n",
        "     \"kkakass\"]\n",
        "with open(\"input.txt\", 'w') as file:\n",
        "    file.writelines(L)"
      ],
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UwEI-ndcVWJk",
        "outputId": "25b4c09b-9af7-4236-8816-3e4957a5e46c"
      },
      "source": [
        "with open(\"input.txt\") as file:\n",
        "    print(file.read())"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "aaaaaaa\n",
            "agajkka\n",
            "kkakass\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "12JtwVSUV2Fb",
        "outputId": "166e5fb7-fc55-4ae0-db45-7cc58e0eba1b"
      },
      "source": [
        "! python"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Python 3.7.11 (default, Jul  3 2021, 18:01:19) \n",
            "[GCC 7.5.0] on linux\n",
            "Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n",
            ">>> \n",
            "KeyboardInterrupt\n",
            ">>> \n",
            "KeyboardInterrupt\n",
            ">>> ^C\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}