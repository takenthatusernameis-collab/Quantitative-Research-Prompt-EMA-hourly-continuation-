# EMA Hourly Continuation — MERL/USDT P26_34

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.3356 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.6268 |
| gross_win_rate | 0.4177 |
| sharpe_ratio | -10.2539 |
| sortino_ratio | -4.7638 |
| max_drawdown | 0.9976 |
| cagr | -0.9096 |
| net_avg_win | 11.6355 |
| net_avg_loss | -23.3861 |
| avg_hold_time_bars | 2.3414 |
| exposure | 0.1147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
