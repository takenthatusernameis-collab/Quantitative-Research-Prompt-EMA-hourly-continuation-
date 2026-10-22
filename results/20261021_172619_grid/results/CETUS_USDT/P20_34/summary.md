# EMA Hourly Continuation — CETUS/USDT P20_34

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6613 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -3.1986 |
| sortino_ratio | -0.9242 |
| max_drawdown | 0.6846 |
| cagr | -0.3465 |
| net_avg_win | 68.6948 |
| net_avg_loss | -85.9573 |
| avg_hold_time_bars | 4.9153 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
