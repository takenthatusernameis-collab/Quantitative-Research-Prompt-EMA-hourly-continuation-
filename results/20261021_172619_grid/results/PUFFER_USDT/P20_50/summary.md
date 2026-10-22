# EMA Hourly Continuation — PUFFER/USDT P20_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8740 |
| net_win_rate | 0.5272 |
| gross_profit_factor | 1.1032 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -0.8703 |
| sortino_ratio | -0.2814 |
| max_drawdown | 0.2446 |
| cagr | -0.1250 |
| net_avg_win | 76.9170 |
| net_avg_loss | -98.1421 |
| avg_hold_time_bars | 8.3193 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
