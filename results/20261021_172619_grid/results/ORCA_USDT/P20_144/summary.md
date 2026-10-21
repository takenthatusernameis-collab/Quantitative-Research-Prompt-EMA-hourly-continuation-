# EMA Hourly Continuation — ORCA/USDT P20_144

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.7562 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9476 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.6738 |
| sortino_ratio | -0.4783 |
| max_drawdown | 0.4889 |
| cagr | -0.2007 |
| net_avg_win | 66.7279 |
| net_avg_loss | -86.0889 |
| avg_hold_time_bars | 30.3975 |
| exposure | 0.5596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
