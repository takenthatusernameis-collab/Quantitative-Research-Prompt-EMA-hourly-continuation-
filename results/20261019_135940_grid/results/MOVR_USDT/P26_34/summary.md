# EMA Hourly Continuation — MOVR/USDT P26_34

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.2319 |
| net_win_rate | 0.3733 |
| gross_profit_factor | 0.7119 |
| gross_win_rate | 0.4221 |
| sharpe_ratio | -12.4151 |
| sortino_ratio | -5.8793 |
| max_drawdown | 0.9995 |
| cagr | -0.9533 |
| net_avg_win | 7.4531 |
| net_avg_loss | -19.1382 |
| avg_hold_time_bars | 2.2912 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
