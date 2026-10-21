# EMA Hourly Continuation — SOL/USDT P89_100

**Symbol:** SOL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 65 |
| net_profit_factor | 0.5996 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -1.2254 |
| sortino_ratio | -0.1419 |
| max_drawdown | 0.1657 |
| cagr | -0.0624 |
| net_avg_win | 72.1977 |
| net_avg_loss | -109.7910 |
| avg_hold_time_bars | 4.6000 |
| exposure | 0.0136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
