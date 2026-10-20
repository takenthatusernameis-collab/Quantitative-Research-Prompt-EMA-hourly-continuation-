# EMA Hourly Continuation — PUNDIX/USDT P8_21

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1501 |
| net_profit_factor | 0.3052 |
| net_win_rate | 0.4031 |
| gross_profit_factor | 0.7232 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -12.4730 |
| sortino_ratio | -6.8678 |
| max_drawdown | 0.9998 |
| cagr | -0.9683 |
| net_avg_win | 7.2578 |
| net_avg_loss | -16.0594 |
| avg_hold_time_bars | 4.0779 |
| exposure | 0.2782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
