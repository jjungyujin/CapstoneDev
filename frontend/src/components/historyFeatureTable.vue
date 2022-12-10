<template>
  <div class="card-body">
    <table v-for ="i in 2" :key="i" class="inputTable">
      <thead>
        <tr>
          <th v-for="j in 6" :key="j">{{FEATURE_names[j + 6*i - 7]}}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td v-for="j in 6" :key="j">
            <input
              :value="FEATURE_values[j + 6*i - 7]"
              type="text"
              class="main-searchbox"
              disabled
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  methods: {},
  props: {
    FEATURE_values: Array
  },
  data() {
    return {
      // FEATURE_values: [
      //   11,
      //   22,
      //   33,
      //   44,
      //   55,
      //   66,
      //   77,
      //   88,
      //   99,
      //   1010,
      //   1111,
      //   1212
      // ],
      FEATURE_names: [
        "코일의 평균 입측 두께",
        "upper 롤 이동값",
        "lower 롤 이동값",
        "밴딩 DS",
        "LH tension",
        "RH tension",
        "POR tension",
        "POR tension (N/mm²)",
        "롤 힘",
        "롤 속도",
        "좌 냉각수 유량",
        "우 냉각수 유량"
      ]
    };
  },
  components: {}
};
</script>
