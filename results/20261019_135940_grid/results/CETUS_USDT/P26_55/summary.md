# EMA Hourly Continuation — CETUS/USDT P26_55

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.5567 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.9074 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -6.6096 |
| sortino_ratio | -2.8320 |
| max_drawdown | 0.9696 |
| cagr | -0.7438 |
| net_avg_win | 29.6416 |
| net_avg_loss | -42.6386 |
| avg_hold_time_bars | 4.4165 |
| exposure | 0.1843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
