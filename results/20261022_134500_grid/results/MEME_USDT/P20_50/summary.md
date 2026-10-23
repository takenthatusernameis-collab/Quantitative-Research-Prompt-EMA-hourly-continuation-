# EMA Hourly Continuation — MEME/USDT P20_50

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1055 |
| net_profit_factor | 0.5357 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.8769 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -6.8811 |
| sortino_ratio | -3.1601 |
| max_drawdown | 0.9788 |
| cagr | -0.7779 |
| net_avg_win | 23.8344 |
| net_avg_loss | -36.1599 |
| avg_hold_time_bars | 4.5943 |
| exposure | 0.2203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
