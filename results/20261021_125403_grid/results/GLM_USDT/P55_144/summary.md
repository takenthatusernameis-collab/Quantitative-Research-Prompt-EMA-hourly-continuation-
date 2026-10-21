# EMA Hourly Continuation — GLM/USDT P55_144

**Symbol:** GLM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7663 |
| net_win_rate | 0.5147 |
| gross_profit_factor | 1.0571 |
| gross_win_rate | 0.5147 |
| sharpe_ratio | -1.6746 |
| sortino_ratio | -0.4851 |
| max_drawdown | 0.4434 |
| cagr | -0.2001 |
| net_avg_win | 67.0154 |
| net_avg_loss | -92.7554 |
| avg_hold_time_bars | 12.3309 |
| exposure | 0.2287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
