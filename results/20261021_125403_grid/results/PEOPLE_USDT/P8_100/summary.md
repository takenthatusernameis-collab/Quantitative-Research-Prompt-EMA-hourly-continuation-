# EMA Hourly Continuation — PEOPLE/USDT P8_100

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.8982 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -1.7032 |
| sortino_ratio | -0.4903 |
| max_drawdown | 0.4563 |
| cagr | -0.2027 |
| net_avg_win | 74.8442 |
| net_avg_loss | -87.3183 |
| avg_hold_time_bars | 37.6626 |
| exposure | 0.7022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
