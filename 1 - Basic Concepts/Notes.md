# Basic Concepts

## List, Tuple, Dictionary, Set

### Difference

| List               | Tuple     | Dictionary  | Set           |
| ------------------ | --------- | ----------- | ------------- |
| Ordered            | Ordered   | Key-Value   | Unordered     |
| Mutable            | Immutable | Mutable     | Mutable       |
| Duplicates allowed | Allowed   | Keys unique | No duplicates |
| Indexed            | Indexed   | By key      | Not indexed   |

### Use Cases

| Situation                                           | Use        |
| --------------------------------------------------- | ---------- |
| Ordered collection you need to modify               | List       |
| Fixed values that shouldn't change                  | Tuple      |
| Store data by names (key-value pairs)               | Dictionary |
| Remove duplicates or perform fast membership checks | Set        |

### Commonly used functions

| Function      | Mental model         |
| ------------- | -------------------- |
| `enumerate()` | index + value        |
| `zip()`       | pair things together |
| `map()`       | transform everything |
| `filter()`    | keep matching items  |
| `any()`       | at least one?        |
| `all()`       | everyone?            |
| `sum()`       | total                |
| `min()`       | smallest             |
| `max()`       | largest              |
| `sorted()`    | sorted **new list**  |
| `reversed()`  | reverse iterator     |
