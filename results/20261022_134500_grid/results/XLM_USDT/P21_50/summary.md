# EMA Hourly Continuation — XLM/USDT P21_50

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.2905 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -9.1228 |
| sortino_ratio | -4.1091 |
| max_drawdown | 0.9947 |
| cagr | -0.8745 |
| net_avg_win | 9.1323 |
| net_avg_loss | -24.3801 |
| avg_hold_time_bars | 4.5671 |
| exposure | 0.2120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
