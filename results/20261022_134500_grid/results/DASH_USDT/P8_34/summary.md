# EMA Hourly Continuation — DASH/USDT P8_34

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1393 |
| net_profit_factor | 0.3677 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8876 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -8.7892 |
| sortino_ratio | -4.5993 |
| max_drawdown | 0.9968 |
| cagr | -0.8988 |
| net_avg_win | 9.1440 |
| net_avg_loss | -20.7714 |
| avg_hold_time_bars | 5.4192 |
| exposure | 0.3431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
