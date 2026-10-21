# EMA Hourly Continuation — RUNE/USDT P55_200

**Symbol:** RUNE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 1.0356 |
| net_win_rate | 0.5602 |
| gross_profit_factor | 1.2740 |
| gross_win_rate | 0.5602 |
| sharpe_ratio | 0.2095 |
| sortino_ratio | 0.0474 |
| max_drawdown | 0.1895 |
| cagr | 0.0158 |
| net_avg_win | 86.4114 |
| net_avg_loss | -106.2650 |
| avg_hold_time_bars | 40.1950 |
| exposure | 0.4403 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
