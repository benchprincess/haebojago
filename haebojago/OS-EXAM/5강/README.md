#### 배열의 특징 및 연결리스트 구조

- 배열은 인덱스를 통해 데이터에 직접적인 접근이 가능하기 때문에 접근이 아주 빠르다는 장점이 있다. 그러나 배열 내의 데이터 이동 및 재구성이 굉장히 힘들다. 배열에서 원소를 하나 삭제하려면 그 뒤에 있는 원소들을 전부 한 칸씩 당겨야 하고, 원소를 삽입하려면 그 뒤에 있는 원소들을 전부 한칸 씩 밀어야한다. 또한 배열의 크기는 초기에 설정하면 그 이후에 변경이 불가능하다. 초기에 설정한 크기를 넘어가면 데이터 삽입을 위해 원소 하나를 지워줘야 한다. 마지막으로 메모리 관점에서 봤을때 배열은 연속 할당 된다는 특징이 있다. 여러모로 메모리 사용이 비효율적이다.

- 배열의 이러한 단점들이 연결리스트에서는 해결된다. 연결리스트는 필요할때마다 데이터를 생성하여 연결해주기만 하면 되기 때문에 메모리를 효율적으로 사용할 수 있다. 메모리 관점으로 봤을때 연결리스트는 불연속 할당 된다는 특징이 있기 때문에 크기를 늘이고 줄이는데 자유롭다. 그러나 데이터 접근 속도는 느리다는 단점이 있다. 인덱스로 접근이 불가하기 때문에 원하는 데이터를 찾기 위해서는 시작 위치부터 탐색을 진행해야 한다.

#### 연결리스트 구조

- 각 노드는 하나의 포인터와 데이터를 가지고있고 head와 tail은 각각 리스트의 제일 처음과 끝을 말한다. 리스트의 시작점에 대한 정보는 알아야하기 때문에 head는 멤버로 존재해야하지만 tail은 꼭 가지고 있을 필요는 없다. 그 이유는 next 포인터가 null을 참조하는 노드가 tail 이기 떄문에 단일 연결 리스트에서 멤버 변수로 head만 가지고 있는다.

#### 클래스 정의

- 노드 클래스 (SNode)

template <typename E>
class SNode{
    private:
    E elem;                 <!-- 원소값 -->
    SNode<E>* next;         <!-- 리스트의 다음 항목 -->

    template <typename W>
    friend class SLinkedList;
};

- 연결 리스트 클래스 (SLinkedList)

template <typename E>
class SLinkedList{ 
public:
SLinkedList();                      <!-- 생성자 -->
~SLinkedList();                     <!-- 소멸자 -->
bool empty() const;                 <!-- 리스트가 비었는지 -->
const E& front() const;             <!-- head값 반환 -->
    void addFront(const E& e);      <!-- 맨 앞에 노드 추가 -->
    void removeFront();             <!-- 맨 앞의 노드 삭제 -->
    private:
        SNode<E>* head;             <!-- head 노드 포인터 -->
};

#### 구현

- 간단한 멤버 함수를 먼저 구현해보면, 생성자와 소멸자, 빈 리스트 여부, head 값 반환하는 멤버함수는 아래와 같이 구현할 수 있다.

<!-- 생성자 -->
template <typename E>
SLinkedList<E>::SLinkedList():head(NULL){}

<!-- 소멸자 -->
template <typename E>
SLinkedList<E>::~SLinkedList(){
    while(!empty()) removeFront();
}

<!-- 리스트가 비었는지 -->
template <typename E>
bool SLinkedList<E>::empty() const{
    return head == NULL;
}

<!-- head 값 -->
template <typename E>
const E& SLinkedList<E>::front() const{
    return head->elem;
}

- 리스트 생성자는 head 포인터를 NULL로 만들어서 비어있는 리스트를 만든다.
- 소멸자는 리스트에 있는 원소들을 반복적으로 삭제하면 된다.
- 리스트가 비어있는지는 head 포인터가 NULL 인지만 살펴보면 된다.
- head 값 반환은 말 그대로 head의 elem을 반환해주면 된다.


#### 데이터 삽입

- head에 원소를 삽입하는 과정은 먼저 새로운 노드를 만들고, 원하는 문자열을 elem의 값으로 넣어주고 마지막으로 next 연결을 리스트의 현재 head를 가리키도록 만든다. 그 후 head는 새로운 노드를 가리키도록 세팅하면 된다.

<!-- 맨 앞에 노드 추가 -->
template <typename E>
void SLinkedList<E>::addFront(const E& e){
    SNode<E>* v = new SNode<E>;     <!-- 새로운 노드 생성 -->
    v->elem = e;                    <!-- 데이터 저장 -->
    v->next = head;                 <!-- head가 새로운 노드를 가리키도록 -->
    head = v;                       <!-- 새로운 노드를 head로 지정 -->
}


#### 데이터 삭제

- 데이터 삭제는 삽입을 반대로 수행하면 된다. 먼저 기존의 head를 가리키는 포인터를 저장하고, head포인터가 리스트의 다음 노드를 가리키도록 바꿔준다. 그 후 기존의 head 노드를 지운다.

<!-- 맨 앞의 노드 삭제 -->
template <typename E>
void SLinkedList<E>::removeFront(){
    SNode<E>* old = head;   <!-- 이전 head 저장 -->
    head = old->next;       <!-- head 위치 이동 -->
    delete old;             <!-- 이전 head delete -->
}