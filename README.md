# API_CRUD_NOSQL_REST

## **EMPLOYEES**

### ![POST](./assets/img/POST.svg) CREATE POST

```
/api/create-post
```

#### Body

```json
{
  "title": "Exemplo",
  "author": "Thainá Ferreira",
  "tags": ["exemplo", "teste"],
  "content": "Escreva aqui o comentário"
}
```

#### Response

```json
{
  "author": "Thainá Ferreira",
  "content": "Escreva aqui o comentário",
  "created_at": "Wed, 08 Sep 2021 00:33:38 GMT",
  "id": 3,
  "tags": ["exemplo", "teste"],
  "title": "Exemplo"
}
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET ALL POSTS

```
/api/get-posts
```

#### Response

```json
[
  {
    "author": "Thaina Ferreira",
    "content": "Aprendendo a usar pymongo",
    "created_at": "Tue, 07 Sep 2021 23:36:53 GMT",
    "id": 1,
    "tags": ["python", "estudos", "pymongo", "database"],
    "title": "Pymongo"
  },
  {
    "author": "Thaina Ferreira",
    "content": "Primeiro teste de edição de comentário",
    "created_at": "Tue, 07 Sep 2021 23:38:30 GMT",
    "id": 2,
    "tags": ["teste"],
    "title": "Teste",
    "update_at": "Wed, 08 Sep 2021 00:12:10 GMT"
  },
  {
    "author": "Thainá Ferreira",
    "content": "Escreva aqui o contéudo do comentário",
    "created_at": "Wed, 08 Sep 2021 00:33:38 GMT",
    "id": 3,
    "tags": ["exemplo", "teste"],
    "title": "Exemplo"
  }
]
```

<br>
<br>

### ![GET](./assets/img/GET.svg) GET POST BY ID

```
/api/get-post/<int:id>
```

#### Response

```json
{
  "author": "Thainá Ferreira",
  "content": "Escreva aqui o contéudo do comentário",
  "created_at": "Wed, 08 Sep 2021 00:33:38 GMT",
  "id": 3,
  "tags": ["exemplo", "teste"],
  "title": "Exemplo"
}
```

<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE POST BY ID

```
/api/update-post/<int:id>
```

#### Body

```json
{
  "content": "testando edição"
}
```

#### Response

```json
{
  "author": "Thainá Ferreira",
  "content": "Testando edição",
  "created_at": "Wed, 08 Sep 2021 00:33:38 GMT",
  "id": 3,
  "tags": ["exemplo", "teste"],
  "title": "Exemplo",
  "update_at": "Wed, 08 Sep 2021 00:50:08 GMT"
}
```

<br>
<br>

---

### ![DELETE](./assets/img/DELETE.svg) DELETE POST BY ID

```
/api/delete-post/<int:id>
```

#### Response

```json
{
  "author": "Thainá Ferreira",
  "content": "testando edição",
  "created_at": "Wed, 08 Sep 2021 00:33:38 GMT",
  "id": 3,
  "tags": ["exemplo", "teste"],
  "title": "Exemplo",
  "update_at": "Wed, 08 Sep 2021 00:50:08 GMT"
}
```

<br>
<br>
