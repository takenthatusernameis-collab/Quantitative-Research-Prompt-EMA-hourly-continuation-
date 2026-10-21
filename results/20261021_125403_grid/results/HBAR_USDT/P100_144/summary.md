# EMA Hourly Continuation — HBAR/USDT P100_144

**Symbol:** HBAR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.6762 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -1.9317 |
| sortino_ratio | -0.4045 |
| max_drawdown | 0.4150 |
| cagr | -0.1691 |
| net_avg_win | 75.4308 |
| net_avg_loss | -104.4565 |
| avg_hold_time_bars | 6.4695 |
| exposure | 0.0626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
