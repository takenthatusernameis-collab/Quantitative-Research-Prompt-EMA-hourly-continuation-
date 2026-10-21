# EMA Hourly Continuation — LINK/USDT P21_55

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.8842 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -3.0818 |
| sortino_ratio | -0.9394 |
| max_drawdown | 0.6737 |
| cagr | -0.3503 |
| net_avg_win | 59.9373 |
| net_avg_loss | -78.2955 |
| avg_hold_time_bars | 9.2713 |
| exposure | 0.1926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
