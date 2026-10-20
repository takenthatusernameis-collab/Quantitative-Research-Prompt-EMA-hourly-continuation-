# EMA Hourly Continuation — DOGS/USDT P26_55

**Symbol:** DOGS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 841 |
| net_profit_factor | 0.4741 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.7669 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -7.4217 |
| sortino_ratio | -3.2782 |
| max_drawdown | 0.9674 |
| cagr | -0.7962 |
| net_avg_win | 23.8273 |
| net_avg_loss | -38.7254 |
| avg_hold_time_bars | 3.9917 |
| exposure | 0.1781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
