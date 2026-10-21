# EMA Hourly Continuation — GLM/USDT P100_200

**Symbol:** GLM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7257 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 0.9966 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -1.8137 |
| sortino_ratio | -0.4632 |
| max_drawdown | 0.4524 |
| cagr | -0.1934 |
| net_avg_win | 68.9579 |
| net_avg_loss | -95.6199 |
| avg_hold_time_bars | 11.2508 |
| exposure | 0.1631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
