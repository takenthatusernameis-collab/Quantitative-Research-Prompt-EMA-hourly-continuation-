# EMA Hourly Continuation — ORCA/USDT P50_144

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6626 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8614 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -2.4264 |
| sortino_ratio | -0.6690 |
| max_drawdown | 0.5877 |
| cagr | -0.2668 |
| net_avg_win | 59.7140 |
| net_avg_loss | -80.2107 |
| avg_hold_time_bars | 16.2328 |
| exposure | 0.2789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
