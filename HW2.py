# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

int main()
{
    int s, p, y;
    cin >> s >> p;
    for (int x=1; x <= 30000; ++x){
    y=s-x;
    if(x<=y && x*y==p)
        cout << x << " " << y;
    }
    return 0;
}