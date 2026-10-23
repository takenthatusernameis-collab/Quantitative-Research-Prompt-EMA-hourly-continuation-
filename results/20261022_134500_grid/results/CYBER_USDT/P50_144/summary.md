# EMA Hourly Continuation — CYBER/USDT P50_144

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6360 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9578 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -2.9178 |
| sortino_ratio | -0.9169 |
| max_drawdown | 0.6899 |
| cagr | -0.3548 |
| net_avg_win | 47.5997 |
| net_avg_loss | -71.9019 |
| avg_hold_time_bars | 12.8320 |
| exposure | 0.2916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
