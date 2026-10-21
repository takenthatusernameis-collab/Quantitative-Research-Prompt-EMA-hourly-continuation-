# EMA Hourly Continuation — MINA/USDT P8_55

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7859 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.9703 |
| sortino_ratio | -0.7298 |
| max_drawdown | 0.6410 |
| cagr | -0.2870 |
| net_avg_win | 62.1686 |
| net_avg_loss | -80.5325 |
| avg_hold_time_bars | 16.8821 |
| exposure | 0.5141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
