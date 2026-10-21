# EMA Hourly Continuation — EDU/USDT P34_55

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.7810 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -3.4164 |
| sortino_ratio | -0.9921 |
| max_drawdown | 0.6934 |
| cagr | -0.3656 |
| net_avg_win | 46.8599 |
| net_avg_loss | -67.7814 |
| avg_hold_time_bars | 5.7290 |
| exposure | 0.1081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
