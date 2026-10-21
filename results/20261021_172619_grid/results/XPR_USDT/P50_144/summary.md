# EMA Hourly Continuation — XPR/USDT P50_144

**Symbol:** XPR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6626 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8522 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.3086 |
| sortino_ratio | -0.5775 |
| max_drawdown | 0.4858 |
| cagr | -0.2327 |
| net_avg_win | 67.1825 |
| net_avg_loss | -86.2168 |
| avg_hold_time_bars | 14.9903 |
| exposure | 0.2105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
