# EMA Hourly Continuation — ENS/USDT P12_50

**Symbol:** ENS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.7535 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.1999 |
| sortino_ratio | -0.7727 |
| max_drawdown | 0.6050 |
| cagr | -0.2993 |
| net_avg_win | 60.8008 |
| net_avg_loss | -78.3156 |
| avg_hold_time_bars | 12.4279 |
| exposure | 0.3406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
