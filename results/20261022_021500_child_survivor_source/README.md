# How this artifact was built

Source OOS grid scan: `results/20261022_013800_child_oos_grid_scan`.

`survivor_source/cells.jsonl` is the survivor set filtered out of
`results/20261022_013800_child_oos_grid_scan/cells.jsonl`: the cells with at least 30
out-of-sample trades, an out-of-sample net PF above 1 **and** an
out-of-sample net PF still above 1 under the 2x cost stress.
That is 106 cells:

| Symbol | Cell | OOS trades | OOS net PF | OOS 2x-cost net PF |
|---|---|---|---|---|
| AERO/USDT | P12_200 | 79 | 1.1392 | 1.0084 |
| APT/USDT | P12_144 | 86 | 1.1429 | 1.0090 |
| APT/USDT | P12_200 | 36 | 1.3367 | 1.1823 |
| APT/USDT | P20_144 | 90 | 1.2129 | 1.0507 |
| APT/USDT | P21_144 | 93 | 1.2226 | 1.0567 |
| APT/USDT | P26_200 | 80 | 1.2029 | 1.0384 |
| AVA/USDT | P20_200 | 105 | 1.2326 | 1.0120 |
| AVA/USDT | P21_200 | 105 | 1.2324 | 1.0117 |
| AVA/USDT | P26_200 | 99 | 1.2616 | 1.0341 |
| AVA/USDT | P34_200 | 97 | 1.3090 | 1.0502 |
| AVA/USDT | P50_200 | 88 | 1.3796 | 1.0974 |
| BLUR/USDT | P12_144 | 103 | 1.3034 | 1.0910 |
| BLUR/USDT | P12_200 | 86 | 1.2755 | 1.0907 |
| BLUR/USDT | P21_200 | 90 | 1.1885 | 1.0111 |
| BLUR/USDT | P8_144 | 112 | 1.2248 | 1.0202 |
| BLUR/USDT | P8_200 | 83 | 1.2799 | 1.0998 |
| BOME/USDT | P26_200 | 112 | 1.2403 | 1.0411 |
| BRETT/USDT | P8_144 | 78 | 1.2444 | 1.0708 |
| BRETT/USDT | P8_200 | 42 | 1.6802 | 1.5168 |
| CETUS/USDT | P12_200 | 68 | 1.2746 | 1.1305 |
| CETUS/USDT | P8_200 | 85 | 1.4565 | 1.2715 |
| CHZ/USDT | P8_200 | 66 | 1.2395 | 1.0876 |
| COTI/USDT | P50_144 | 115 | 1.2656 | 1.0100 |
| COTI/USDT | P50_200 | 99 | 1.3026 | 1.0675 |
| COTI/USDT | P55_144 | 112 | 1.2911 | 1.0220 |
| DAG/USDT | P8_100 | 109 | 1.3177 | 1.0644 |
| DEXE/USDT | P100_200 | 61 | 1.6140 | 1.3740 |
| DEXE/USDT | P12_100 | 112 | 1.1871 | 1.0349 |
| DEXE/USDT | P12_144 | 88 | 1.3128 | 1.1594 |
| DEXE/USDT | P12_200 | 65 | 1.3968 | 1.2667 |
| DEXE/USDT | P20_144 | 90 | 1.2391 | 1.0938 |
| DEXE/USDT | P20_200 | 66 | 1.6404 | 1.4926 |
| DEXE/USDT | P21_144 | 89 | 1.2166 | 1.0751 |
| DEXE/USDT | P21_200 | 64 | 1.6713 | 1.5219 |
| DEXE/USDT | P26_200 | 63 | 1.2401 | 1.1233 |
| DEXE/USDT | P34_144 | 88 | 1.2222 | 1.0632 |
| DEXE/USDT | P50_144 | 89 | 1.4465 | 1.2605 |
| DEXE/USDT | P50_200 | 70 | 1.7875 | 1.5833 |
| DEXE/USDT | P55_144 | 76 | 1.5373 | 1.3363 |
| DEXE/USDT | P55_200 | 63 | 1.8907 | 1.6783 |
| DEXE/USDT | P89_200 | 56 | 1.7875 | 1.5267 |
| DEXE/USDT | P8_100 | 114 | 1.2379 | 1.0947 |
| DEXE/USDT | P8_144 | 83 | 1.5518 | 1.4012 |
| DEXE/USDT | P8_200 | 56 | 1.3520 | 1.2415 |
| DIA/USDT | P12_200 | 84 | 1.4204 | 1.1836 |
| DIA/USDT | P20_200 | 122 | 1.2927 | 1.0444 |
| DIA/USDT | P21_200 | 120 | 1.3037 | 1.0515 |
| DIA/USDT | P26_200 | 114 | 1.2413 | 1.0018 |
| DIA/USDT | P8_200 | 89 | 1.2169 | 1.0141 |
| EGLD/USDT | P55_200 | 99 | 1.3233 | 1.0262 |
| ENA/USDT | P20_200 | 106 | 1.2024 | 1.0479 |
| ENA/USDT | P20_21 | 46 | 1.3902 | 1.0315 |
| ENA/USDT | P21_200 | 101 | 1.1506 | 1.0041 |
| ENA/USDT | P34_144 | 111 | 1.2519 | 1.0555 |
| ENA/USDT | P8_144 | 123 | 1.2020 | 1.0456 |
| FET/USDT | P12_200 | 36 | 1.5616 | 1.4435 |
| FET/USDT | P20_200 | 34 | 1.2336 | 1.1324 |
| FET/USDT | P21_200 | 39 | 1.1274 | 1.0389 |
| FET/USDT | P8_200 | 45 | 1.2115 | 1.1200 |
| FLUX/USDT | P8_200 | 93 | 1.5170 | 1.2910 |
| GMT/USDT | P12_200 | 83 | 1.1827 | 1.0090 |
| GMT/USDT | P8_144 | 110 | 1.2242 | 1.0183 |
| GMT/USDT | P8_200 | 88 | 1.4737 | 1.2727 |
| GRT/USDT | P20_200 | 57 | 1.4433 | 1.2623 |
| GRT/USDT | P8_200 | 57 | 1.3602 | 1.2002 |
| IMX/USDT | P12_200 | 94 | 1.3886 | 1.1734 |
| IMX/USDT | P20_200 | 122 | 1.3057 | 1.0826 |
| IMX/USDT | P21_200 | 111 | 1.2394 | 1.0252 |
| IMX/USDT | P26_200 | 114 | 1.4801 | 1.2167 |
| IMX/USDT | P34_200 | 101 | 1.3729 | 1.1217 |
| IMX/USDT | P50_200 | 102 | 1.2397 | 1.0012 |
| IMX/USDT | P8_200 | 93 | 1.3049 | 1.1024 |
| JASMY/USDT | P144_200 | 56 | 1.4928 | 1.0550 |
| MEW/USDT | P8_200 | 49 | 1.1845 | 1.0103 |
| MINA/USDT | P12_200 | 75 | 1.2162 | 1.0532 |
| PENDLE/USDT | P34_144 | 98 | 1.3020 | 1.0650 |
| POL/USDT | P20_200 | 69 | 1.3597 | 1.1617 |
| POL/USDT | P21_200 | 71 | 1.4246 | 1.2155 |
| POL/USDT | P26_200 | 71 | 1.3900 | 1.1647 |
| POL/USDT | P34_200 | 95 | 1.3951 | 1.1151 |
| POL/USDT | P8_200 | 52 | 1.6086 | 1.3857 |
| PUFFER/USDT | P20_200 | 81 | 1.3768 | 1.2245 |
| PUFFER/USDT | P21_200 | 75 | 1.3497 | 1.1974 |
| PUFFER/USDT | P26_200 | 75 | 1.2674 | 1.1244 |
| PYTH/USDT | P8_200 | 82 | 1.1827 | 1.0553 |
| RENDER/USDT | P8_200 | 45 | 1.1898 | 1.0722 |
| ROSE/USDT | P12_200 | 55 | 1.1550 | 1.0027 |
| ROSE/USDT | P34_200 | 88 | 1.3328 | 1.1080 |
| ROSE/USDT | P55_200 | 112 | 1.3264 | 1.0651 |
| RUNE/USDT | P50_144 | 120 | 1.5230 | 1.0963 |
| RUNE/USDT | P50_200 | 89 | 1.3239 | 1.0048 |
| SUPER/USDT | P8_200 | 64 | 1.2855 | 1.0890 |
| SYN/USDT | P20_200 | 99 | 1.2628 | 1.0678 |
| SYN/USDT | P26_200 | 91 | 1.1537 | 1.0032 |
| TWT/USDT | P8_200 | 73 | 1.2604 | 1.0174 |
| T/USDT | P12_200 | 52 | 1.3272 | 1.0711 |
| VELO/USDT | P12_200 | 114 | 1.2723 | 1.1009 |
| VELO/USDT | P20_200 | 107 | 1.2339 | 1.0705 |
| WIN/USDT | P12_200 | 96 | 1.2759 | 1.0616 |
| WIN/USDT | P8_200 | 104 | 1.2949 | 1.0848 |
| WLD/USDT | P20_200 | 94 | 1.3171 | 1.1761 |
| WLD/USDT | P21_200 | 103 | 1.2454 | 1.1119 |
| W/USDT | P12_200 | 80 | 1.2138 | 1.0512 |
| XPR/USDT | P8_200 | 44 | 1.5710 | 1.3538 |
| ZEN/USDT | P12_200 | 37 | 1.2002 | 1.0623 |
| ZEN/USDT | P8_200 | 33 | 1.4808 | 1.3582 |

Command:

```python
for row in json.load(open('results/20261022_013800_child_oos_grid_scan/cells.jsonl')):
    if (row['oos_trades'] or 0) >= 30 \
            and (row['oos_net_pf'] or 0.0) > 1.0 \
            and (row['oos_stress_net_pf'] or 0.0) > 1.0:
        keep(row)
```
