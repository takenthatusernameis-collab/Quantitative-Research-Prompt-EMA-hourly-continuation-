# EMA Hourly Continuation — MOVR/USDT P26_200

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7909 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9349 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.2592 |
| sortino_ratio | -0.3259 |
| max_drawdown | 0.3693 |
| cagr | -0.1407 |
| net_avg_win | 74.3728 |
| net_avg_loss | -89.5885 |
| avg_hold_time_bars | 36.8697 |
| exposure | 0.5530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
