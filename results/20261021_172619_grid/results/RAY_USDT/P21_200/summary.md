# EMA Hourly Continuation — RAY/USDT P21_200

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7875 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -1.2940 |
| sortino_ratio | -0.3132 |
| max_drawdown | 0.3545 |
| cagr | -0.1351 |
| net_avg_win | 81.4232 |
| net_avg_loss | -95.8103 |
| avg_hold_time_bars | 46.7024 |
| exposure | 0.6135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
