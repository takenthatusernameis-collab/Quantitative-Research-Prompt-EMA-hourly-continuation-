# EMA Hourly Continuation — AVAX/USDT P26_55

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.5291 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -7.5697 |
| sortino_ratio | -3.1432 |
| max_drawdown | 0.9810 |
| cagr | -0.7896 |
| net_avg_win | 28.4561 |
| net_avg_loss | -43.4511 |
| avg_hold_time_bars | 4.0000 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
