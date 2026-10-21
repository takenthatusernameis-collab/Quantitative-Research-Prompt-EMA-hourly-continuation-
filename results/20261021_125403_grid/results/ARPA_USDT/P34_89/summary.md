# EMA Hourly Continuation — ARPA/USDT P34_89

**Symbol:** ARPA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.5966 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -3.7847 |
| sortino_ratio | -1.1988 |
| max_drawdown | 0.7665 |
| cagr | -0.4245 |
| net_avg_win | 50.5405 |
| net_avg_loss | -67.0399 |
| avg_hold_time_bars | 10.7550 |
| exposure | 0.2424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
