# EMA Hourly Continuation — FLIP/USDT P12_144

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.6781 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -2.2216 |
| sortino_ratio | -0.5656 |
| max_drawdown | 0.5160 |
| cagr | -0.2335 |
| net_avg_win | 67.0816 |
| net_avg_loss | -86.4863 |
| avg_hold_time_bars | 45.4634 |
| exposure | 0.6778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
