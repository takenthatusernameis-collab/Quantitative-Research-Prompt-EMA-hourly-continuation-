# EMA Hourly Continuation — BTT/USDT P21_200

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.4383 |
| net_win_rate | 0.4218 |
| gross_profit_factor | 0.7735 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -4.2410 |
| sortino_ratio | -1.0185 |
| max_drawdown | 0.7335 |
| cagr | -0.4006 |
| net_avg_win | 45.5180 |
| net_avg_loss | -75.7577 |
| avg_hold_time_bars | 50.7959 |
| exposure | 0.6788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
