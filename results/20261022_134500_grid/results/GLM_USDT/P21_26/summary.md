# EMA Hourly Continuation — GLM/USDT P21_26

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1137 |
| net_profit_factor | 0.2311 |
| net_win_rate | 0.3597 |
| gross_profit_factor | 0.7580 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -13.7893 |
| sortino_ratio | -6.7575 |
| max_drawdown | 0.9999 |
| cagr | -0.9725 |
| net_avg_win | 7.3481 |
| net_avg_loss | -17.8629 |
| avg_hold_time_bars | 2.6350 |
| exposure | 0.1362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
