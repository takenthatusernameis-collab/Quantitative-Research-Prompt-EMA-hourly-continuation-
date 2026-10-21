# EMA Hourly Continuation — GLM/USDT P21_55

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.6362 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9064 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -3.6504 |
| sortino_ratio | -1.2548 |
| max_drawdown | 0.7746 |
| cagr | -0.4393 |
| net_avg_win | 48.9007 |
| net_avg_loss | -68.6008 |
| avg_hold_time_bars | 8.7126 |
| exposure | 0.2301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
