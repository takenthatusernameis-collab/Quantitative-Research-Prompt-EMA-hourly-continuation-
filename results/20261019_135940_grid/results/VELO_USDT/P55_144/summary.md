# EMA Hourly Continuation — VELO/USDT P55_144

**Symbol:** VELO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.7199 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0088 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -2.2889 |
| sortino_ratio | -0.7512 |
| max_drawdown | 0.6217 |
| cagr | -0.3010 |
| net_avg_win | 56.0580 |
| net_avg_loss | -79.3243 |
| avg_hold_time_bars | 9.8850 |
| exposure | 0.2422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
