# EMA Hourly Continuation — IOST/USDT P20_55

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.4600 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -7.1304 |
| sortino_ratio | -3.0059 |
| max_drawdown | 0.9761 |
| cagr | -0.7717 |
| net_avg_win | 20.7720 |
| net_avg_loss | -36.7150 |
| avg_hold_time_bars | 6.3531 |
| exposure | 0.2576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
