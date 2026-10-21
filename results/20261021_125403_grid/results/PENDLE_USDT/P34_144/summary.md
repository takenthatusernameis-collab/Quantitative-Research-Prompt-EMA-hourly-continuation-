# EMA Hourly Continuation — PENDLE/USDT P34_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8413 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 0.9985 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -0.9224 |
| sortino_ratio | -0.2527 |
| max_drawdown | 0.3909 |
| cagr | -0.1118 |
| net_avg_win | 74.1900 |
| net_avg_loss | -89.6506 |
| avg_hold_time_bars | 25.2959 |
| exposure | 0.4197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
