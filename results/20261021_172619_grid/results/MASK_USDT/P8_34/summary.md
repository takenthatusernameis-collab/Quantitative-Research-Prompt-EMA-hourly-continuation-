# EMA Hourly Continuation — MASK/USDT P8_34

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9464 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -3.9823 |
| sortino_ratio | -1.6085 |
| max_drawdown | 0.8447 |
| cagr | -0.5236 |
| net_avg_win | 41.1557 |
| net_avg_loss | -58.3931 |
| avg_hold_time_bars | 9.7890 |
| exposure | 0.3564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
