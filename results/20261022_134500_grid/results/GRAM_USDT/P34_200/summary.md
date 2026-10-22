# EMA Hourly Continuation — GRAM/USDT P34_200

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.4490 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.7378 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -4.5262 |
| sortino_ratio | -1.2796 |
| max_drawdown | 0.8060 |
| cagr | -0.4677 |
| net_avg_win | 36.7933 |
| net_avg_loss | -61.9001 |
| avg_hold_time_bars | 27.5868 |
| exposure | 0.5129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
