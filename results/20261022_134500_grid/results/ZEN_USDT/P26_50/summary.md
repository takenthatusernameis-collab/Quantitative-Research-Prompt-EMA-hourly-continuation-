# EMA Hourly Continuation — ZEN/USDT P26_50

**Symbol:** ZEN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.4039 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -8.6460 |
| sortino_ratio | -3.8862 |
| max_drawdown | 0.9924 |
| cagr | -0.8563 |
| net_avg_win | 15.6363 |
| net_avg_loss | -28.1676 |
| avg_hold_time_bars | 3.6072 |
| exposure | 0.1674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
