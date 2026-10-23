# EMA Hourly Continuation — RSR/USDT P50_144

**Symbol:** RSR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7390 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0296 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -1.9766 |
| sortino_ratio | -0.6036 |
| max_drawdown | 0.5188 |
| cagr | -0.2499 |
| net_avg_win | 61.9755 |
| net_avg_loss | -85.3124 |
| avg_hold_time_bars | 13.3562 |
| exposure | 0.2829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
