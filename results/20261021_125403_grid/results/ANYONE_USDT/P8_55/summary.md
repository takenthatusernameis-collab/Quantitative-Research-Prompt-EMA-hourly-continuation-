# EMA Hourly Continuation — ANYONE/USDT P8_55

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.8217 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9520 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.7103 |
| sortino_ratio | -0.6485 |
| max_drawdown | 0.5294 |
| cagr | -0.2613 |
| net_avg_win | 73.6811 |
| net_avg_loss | -85.2644 |
| avg_hold_time_bars | 13.9135 |
| exposure | 0.4471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
