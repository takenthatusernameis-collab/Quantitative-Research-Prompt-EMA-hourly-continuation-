# EMA Hourly Continuation — SNX/USDT P21_26

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.2481 |
| net_win_rate | 0.3871 |
| gross_profit_factor | 0.8255 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -13.1313 |
| sortino_ratio | -6.4694 |
| max_drawdown | 0.9998 |
| cagr | -0.9667 |
| net_avg_win | 7.3160 |
| net_avg_loss | -18.6241 |
| avg_hold_time_bars | 1.9399 |
| exposure | 0.1023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
