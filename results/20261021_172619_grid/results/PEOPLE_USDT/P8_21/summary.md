# EMA Hourly Continuation — PEOPLE/USDT P8_21

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.7176 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -3.2728 |
| sortino_ratio | -1.1697 |
| max_drawdown | 0.7555 |
| cagr | -0.4149 |
| net_avg_win | 63.2137 |
| net_avg_loss | -79.0663 |
| avg_hold_time_bars | 5.9222 |
| exposure | 0.1688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
