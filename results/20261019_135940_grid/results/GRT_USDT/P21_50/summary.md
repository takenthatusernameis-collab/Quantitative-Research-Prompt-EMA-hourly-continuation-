# EMA Hourly Continuation — GRT/USDT P21_50

**Symbol:** GRT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.4994 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8505 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -7.1544 |
| sortino_ratio | -3.1351 |
| max_drawdown | 0.9794 |
| cagr | -0.7844 |
| net_avg_win | 22.5050 |
| net_avg_loss | -36.3543 |
| avg_hold_time_bars | 4.2305 |
| exposure | 0.1861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
