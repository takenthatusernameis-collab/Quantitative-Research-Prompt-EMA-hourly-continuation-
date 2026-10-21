# EMA Hourly Continuation — ICP/USDT P34_55

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.0665 |
| sortino_ratio | -0.4886 |
| max_drawdown | 0.4484 |
| cagr | -0.2003 |
| net_avg_win | 67.3600 |
| net_avg_loss | -92.3931 |
| avg_hold_time_bars | 5.8462 |
| exposure | 0.0725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
