# EMA Hourly Continuation — ORCA/USDT P26_89

**Symbol:** ORCA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6616 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 1.0216 |
| gross_win_rate | 0.5098 |
| sharpe_ratio | -3.4907 |
| sortino_ratio | -1.2665 |
| max_drawdown | 0.8006 |
| cagr | -0.4552 |
| net_avg_win | 46.9152 |
| net_avg_loss | -68.6015 |
| avg_hold_time_bars | 10.6606 |
| exposure | 0.3213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
