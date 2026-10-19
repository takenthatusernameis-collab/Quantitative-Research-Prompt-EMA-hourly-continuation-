# EMA Hourly Continuation — IOTA/USDT P20_34

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.3184 |
| net_win_rate | 0.4056 |
| gross_profit_factor | 0.8070 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -10.9640 |
| sortino_ratio | -5.3020 |
| max_drawdown | 0.9987 |
| cagr | -0.9298 |
| net_avg_win | 10.0101 |
| net_avg_loss | -21.4524 |
| avg_hold_time_bars | 2.8129 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
