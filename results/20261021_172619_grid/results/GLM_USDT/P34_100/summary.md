# EMA Hourly Continuation — GLM/USDT P34_100

**Symbol:** GLM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7727 |
| net_win_rate | 0.5232 |
| gross_profit_factor | 1.0749 |
| gross_win_rate | 0.5232 |
| sharpe_ratio | -1.7061 |
| sortino_ratio | -0.5445 |
| max_drawdown | 0.4939 |
| cagr | -0.2227 |
| net_avg_win | 61.5241 |
| net_avg_loss | -87.3850 |
| avg_hold_time_bars | 11.3576 |
| exposure | 0.2555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
