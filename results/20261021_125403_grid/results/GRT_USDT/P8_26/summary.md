# EMA Hourly Continuation — GRT/USDT P8_26

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6705 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -3.4193 |
| sortino_ratio | -1.2550 |
| max_drawdown | 0.7769 |
| cagr | -0.4375 |
| net_avg_win | 49.9541 |
| net_avg_loss | -66.2212 |
| avg_hold_time_bars | 6.6471 |
| exposure | 0.1994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
