# EMA Hourly Continuation — METIS/USDT P20_55

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.4931 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8403 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -7.0868 |
| sortino_ratio | -3.1090 |
| max_drawdown | 0.9791 |
| cagr | -0.7788 |
| net_avg_win | 22.4241 |
| net_avg_loss | -35.7068 |
| avg_hold_time_bars | 5.4896 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
