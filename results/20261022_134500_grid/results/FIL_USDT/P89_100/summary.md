# EMA Hourly Continuation — FIL/USDT P89_100

**Symbol:** FIL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.2279 |
| net_win_rate | 0.3809 |
| gross_profit_factor | 0.7730 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -9.5386 |
| sortino_ratio | -3.3333 |
| max_drawdown | 0.9895 |
| cagr | -0.8355 |
| net_avg_win | 13.3300 |
| net_avg_loss | -35.9880 |
| avg_hold_time_bars | 2.0226 |
| exposure | 0.0529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
