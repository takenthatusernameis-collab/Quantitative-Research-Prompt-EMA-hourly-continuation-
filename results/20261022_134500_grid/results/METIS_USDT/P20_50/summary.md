# EMA Hourly Continuation — METIS/USDT P20_50

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.4918 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8672 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -7.3576 |
| sortino_ratio | -3.3103 |
| max_drawdown | 0.9841 |
| cagr | -0.8014 |
| net_avg_win | 20.9517 |
| net_avg_loss | -34.2898 |
| avg_hold_time_bars | 4.7878 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
