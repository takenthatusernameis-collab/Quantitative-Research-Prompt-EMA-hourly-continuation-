# EMA Hourly Continuation — LQTY/USDT P21_26

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0201 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -2.1161 |
| sortino_ratio | -0.5055 |
| max_drawdown | 0.4712 |
| cagr | -0.2057 |
| net_avg_win | 65.6731 |
| net_avg_loss | -98.0748 |
| avg_hold_time_bars | 4.7473 |
| exposure | 0.0595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
