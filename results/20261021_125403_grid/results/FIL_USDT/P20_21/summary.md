# EMA Hourly Continuation — FIL/USDT P20_21

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 111 |
| net_profit_factor | 0.5111 |
| net_win_rate | 0.4144 |
| gross_profit_factor | 0.7223 |
| gross_win_rate | 0.4144 |
| sharpe_ratio | -2.2319 |
| sortino_ratio | -0.3349 |
| max_drawdown | 0.3375 |
| cagr | -0.1429 |
| net_avg_win | 72.9652 |
| net_avg_loss | -101.0298 |
| avg_hold_time_bars | 4.5946 |
| exposure | 0.0232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
