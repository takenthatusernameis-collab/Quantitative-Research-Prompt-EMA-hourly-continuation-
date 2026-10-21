# EMA Hourly Continuation — ORCA/USDT P55_144

**Symbol:** ORCA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6573 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8601 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -2.4584 |
| sortino_ratio | -0.6762 |
| max_drawdown | 0.5900 |
| cagr | -0.2692 |
| net_avg_win | 59.0787 |
| net_avg_loss | -79.9386 |
| avg_hold_time_bars | 15.1144 |
| exposure | 0.2583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
