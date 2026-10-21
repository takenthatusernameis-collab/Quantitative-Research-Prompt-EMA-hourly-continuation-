# EMA Hourly Continuation — 1INCH/USDT P20_21

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 152 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0667 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -1.5786 |
| sortino_ratio | -0.2805 |
| max_drawdown | 0.3060 |
| cagr | -0.1211 |
| net_avg_win | 73.2287 |
| net_avg_loss | -114.5950 |
| avg_hold_time_bars | 4.4605 |
| exposure | 0.0308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
