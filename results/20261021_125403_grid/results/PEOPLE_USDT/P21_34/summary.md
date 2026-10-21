# EMA Hourly Continuation — PEOPLE/USDT P21_34

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7402 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0158 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.8851 |
| sortino_ratio | -0.5004 |
| max_drawdown | 0.5089 |
| cagr | -0.2045 |
| net_avg_win | 72.6340 |
| net_avg_loss | -98.6972 |
| avg_hold_time_bars | 5.5015 |
| exposure | 0.0854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
