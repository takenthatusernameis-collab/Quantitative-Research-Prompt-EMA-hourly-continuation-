# EMA Hourly Continuation — ASTR/USDT P20_50

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9726 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -3.0786 |
| sortino_ratio | -1.0460 |
| max_drawdown | 0.7079 |
| cagr | -0.3820 |
| net_avg_win | 52.8452 |
| net_avg_loss | -75.6823 |
| avg_hold_time_bars | 7.8584 |
| exposure | 0.2009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
