# EMA Hourly Continuation — VR/USDT P21_55

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.6503 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8713 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.6964 |
| sortino_ratio | -0.7363 |
| max_drawdown | 0.5830 |
| cagr | -0.2895 |
| net_avg_win | 62.2824 |
| net_avg_loss | -83.2003 |
| avg_hold_time_bars | 11.9027 |
| exposure | 0.2002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
