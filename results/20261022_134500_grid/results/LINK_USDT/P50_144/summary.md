# EMA Hourly Continuation — LINK/USDT P50_144

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6204 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9923 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -3.3695 |
| sortino_ratio | -1.0240 |
| max_drawdown | 0.7284 |
| cagr | -0.3899 |
| net_avg_win | 50.9603 |
| net_avg_loss | -78.3598 |
| avg_hold_time_bars | 12.0535 |
| exposure | 0.2559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
