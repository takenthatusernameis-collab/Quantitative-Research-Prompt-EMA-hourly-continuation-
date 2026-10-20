# EMA Hourly Continuation — TRB/USDT P26_144

**Symbol:** TRB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.6450 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -3.0012 |
| sortino_ratio | -0.9634 |
| max_drawdown | 0.6821 |
| cagr | -0.3601 |
| net_avg_win | 49.6931 |
| net_avg_loss | -71.5454 |
| avg_hold_time_bars | 21.0604 |
| exposure | 0.4889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
