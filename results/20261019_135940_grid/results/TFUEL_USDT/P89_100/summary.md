# EMA Hourly Continuation — TFUEL/USDT P89_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.2622 |
| net_win_rate | 0.3234 |
| gross_profit_factor | 0.7523 |
| gross_win_rate | 0.3704 |
| sharpe_ratio | -12.4181 |
| sortino_ratio | -4.8712 |
| max_drawdown | 0.9988 |
| cagr | -0.9309 |
| net_avg_win | 15.6346 |
| net_avg_loss | -28.4995 |
| avg_hold_time_bars | 2.6652 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
