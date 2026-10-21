# EMA Hourly Continuation — GLM/USDT P34_144

**Symbol:** GLM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.7660 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0270 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.6655 |
| sortino_ratio | -0.4912 |
| max_drawdown | 0.4459 |
| cagr | -0.2029 |
| net_avg_win | 65.8136 |
| net_avg_loss | -89.2185 |
| avg_hold_time_bars | 18.5283 |
| exposure | 0.3571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
