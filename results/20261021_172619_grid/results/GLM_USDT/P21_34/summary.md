# EMA Hourly Continuation — GLM/USDT P21_34

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.5700 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.9060 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -4.5854 |
| sortino_ratio | -1.4279 |
| max_drawdown | 0.8303 |
| cagr | -0.4843 |
| net_avg_win | 50.4332 |
| net_avg_loss | -72.7680 |
| avg_hold_time_bars | 5.4322 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
