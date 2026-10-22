# EMA Hourly Continuation — DOT/USDT P8_200

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.5905 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8996 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.5770 |
| sortino_ratio | -0.5946 |
| max_drawdown | 0.5332 |
| cagr | -0.2563 |
| net_avg_win | 58.1942 |
| net_avg_loss | -86.5604 |
| avg_hold_time_bars | 66.6475 |
| exposure | 0.8422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
