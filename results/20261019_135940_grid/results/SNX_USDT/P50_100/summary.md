# EMA Hourly Continuation — SNX/USDT P50_100

**Symbol:** SNX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.1700 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -3.8695 |
| sortino_ratio | -1.3714 |
| max_drawdown | 0.8249 |
| cagr | -0.4929 |
| net_avg_win | 49.1218 |
| net_avg_loss | -75.7279 |
| avg_hold_time_bars | 5.8613 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
