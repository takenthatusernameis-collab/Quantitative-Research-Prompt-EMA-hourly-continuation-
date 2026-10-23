# EMA Hourly Continuation — AVA/USDT P50_144

**Symbol:** AVA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6337 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 0.9656 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -2.7248 |
| sortino_ratio | -0.8601 |
| max_drawdown | 0.6774 |
| cagr | -0.3353 |
| net_avg_win | 44.3942 |
| net_avg_loss | -71.1928 |
| avg_hold_time_bars | 11.5464 |
| exposure | 0.2603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
