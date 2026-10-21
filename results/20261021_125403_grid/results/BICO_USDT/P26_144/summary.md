# EMA Hourly Continuation — BICO/USDT P26_144

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7015 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8406 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -1.9477 |
| sortino_ratio | -0.5290 |
| max_drawdown | 0.5061 |
| cagr | -0.2165 |
| net_avg_win | 63.3232 |
| net_avg_loss | -78.2952 |
| avg_hold_time_bars | 30.1311 |
| exposure | 0.5013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
