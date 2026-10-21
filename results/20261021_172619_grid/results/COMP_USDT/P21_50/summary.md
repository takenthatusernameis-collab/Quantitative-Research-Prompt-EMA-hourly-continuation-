# EMA Hourly Continuation — COMP/USDT P21_50

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.6149 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.8822 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -3.3204 |
| sortino_ratio | -1.1491 |
| max_drawdown | 0.7650 |
| cagr | -0.4095 |
| net_avg_win | 41.3945 |
| net_avg_loss | -63.2908 |
| avg_hold_time_bars | 7.4726 |
| exposure | 0.1984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
