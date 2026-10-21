# EMA Hourly Continuation — ORBS/USDT P12_20

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.4890 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.8115 |
| gross_win_rate | 0.4075 |
| sharpe_ratio | -5.4870 |
| sortino_ratio | -1.6263 |
| max_drawdown | 0.8523 |
| cagr | -0.5292 |
| net_avg_win | 46.6986 |
| net_avg_loss | -65.6821 |
| avg_hold_time_bars | 7.9461 |
| exposure | 0.1542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
