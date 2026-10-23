# EMA Hourly Continuation — PUNDIX/USDT P20_26

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1221 |
| net_profit_factor | 0.1730 |
| net_win_rate | 0.3481 |
| gross_profit_factor | 0.5855 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -14.7562 |
| sortino_ratio | -7.5033 |
| max_drawdown | 1.0000 |
| cagr | -0.9808 |
| net_avg_win | 4.9219 |
| net_avg_loss | -15.1901 |
| avg_hold_time_bars | 2.8116 |
| exposure | 0.1560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
