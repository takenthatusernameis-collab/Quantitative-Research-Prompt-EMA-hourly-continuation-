# EMA Hourly Continuation — SYN/USDT P20_21

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.5641 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.7971 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -2.7889 |
| sortino_ratio | -0.5903 |
| max_drawdown | 0.5168 |
| cagr | -0.2385 |
| net_avg_win | 66.8200 |
| net_avg_loss | -91.6995 |
| avg_hold_time_bars | 4.4091 |
| exposure | 0.0441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
