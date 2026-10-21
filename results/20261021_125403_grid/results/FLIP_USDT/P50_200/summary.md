# EMA Hourly Continuation — FLIP/USDT P50_200

**Symbol:** FLIP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.5996 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.7721 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -2.4376 |
| sortino_ratio | -0.5325 |
| max_drawdown | 0.4884 |
| cagr | -0.2210 |
| net_avg_win | 65.8130 |
| net_avg_loss | -86.1845 |
| avg_hold_time_bars | 35.1784 |
| exposure | 0.3854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
