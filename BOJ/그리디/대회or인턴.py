# https://www.acmicpc.net/problem/2875
"""
문제
백준대학교는 뛰어난 인재들이 많아 올해에도 N명의 여학생과 M명의 남학생이 팀원을 찾고 있다. 대회에 참여하려는 학생들 중 K명은 반드시 인턴쉽 프로그램에 참여해야 한다. 인턴쉽에 참여하는 학생은 대회에 참여하지 못한다.
백준대학교에서는 뛰어난 인재들이 많기 때문에, 많은 팀을 만드는 것이 최선이다.
여러분은 여학생의 수 N, 남학생의 수 M, 인턴쉽에 참여해야하는 인원 K가 주어질 때 만들 수 있는 최대의 팀 수를 구하면 된다.

입력
첫째 줄에 N, M, K가 순서대로 주어진다. (0 ≤ M ≤ 100, 0 ≤ N ≤ 100, 0 ≤ K ≤ M+N)

출력
만들 수 있는 팀의 최대 개수을 출력하면 된다.
"""
import sys
input = sys.stdin.readline
woman, man, k = map(int, input().split())
team = 0

while woman >= 2 and man >= 1 and woman+man >= k + 3:
    woman -= 2
    man -= 1
    team += 1
print(team)
