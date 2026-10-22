# EMA Hourly Continuation — SQD/USDT P50_144

**Symbol:** SQD/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.9156 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0855 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -0.4824 |
| sortino_ratio | -0.1287 |
| max_drawdown | 0.2047 |
| cagr | -0.0612 |
| net_avg_win | 89.2122 |
| net_avg_loss | -106.0169 |
| avg_hold_time_bars | 16.1747 |
| exposure | 0.2524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
