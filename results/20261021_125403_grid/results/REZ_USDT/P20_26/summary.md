# EMA Hourly Continuation — REZ/USDT P20_26

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.5415 |
| net_win_rate | 0.4164 |
| gross_profit_factor | 0.7311 |
| gross_win_rate | 0.4164 |
| sharpe_ratio | -3.3454 |
| sortino_ratio | -0.7846 |
| max_drawdown | 0.6097 |
| cagr | -0.3050 |
| net_avg_win | 62.5850 |
| net_avg_loss | -82.4459 |
| avg_hold_time_bars | 5.7881 |
| exposure | 0.0718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
