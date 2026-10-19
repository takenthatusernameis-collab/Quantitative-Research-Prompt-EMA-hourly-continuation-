# EMA Hourly Continuation — XMR/USDT P21_144

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.5051 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -6.2523 |
| sortino_ratio | -2.4923 |
| max_drawdown | 0.9546 |
| cagr | -0.7066 |
| net_avg_win | 26.8991 |
| net_avg_loss | -42.9348 |
| avg_hold_time_bars | 12.8286 |
| exposure | 0.4729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
