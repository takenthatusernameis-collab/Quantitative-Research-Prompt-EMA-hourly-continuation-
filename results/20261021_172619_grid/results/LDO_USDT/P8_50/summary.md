# EMA Hourly Continuation — LDO/USDT P8_50

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.2675 |
| sortino_ratio | -0.8429 |
| max_drawdown | 0.6323 |
| cagr | -0.3219 |
| net_avg_win | 59.6806 |
| net_avg_loss | -73.5208 |
| avg_hold_time_bars | 13.6112 |
| exposure | 0.4201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
