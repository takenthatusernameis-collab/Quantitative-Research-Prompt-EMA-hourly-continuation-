# EMA Hourly Continuation — HTX/USDT P21_26

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1344 |
| net_profit_factor | 0.0571 |
| net_win_rate | 0.1600 |
| gross_profit_factor | 0.3419 |
| gross_win_rate | 0.2790 |
| sharpe_ratio | -24.3517 |
| sortino_ratio | -15.1224 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 2.8157 |
| net_avg_loss | -9.3936 |
| avg_hold_time_bars | 2.4315 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
