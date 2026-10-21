# EMA Hourly Continuation — RLC/USDT P26_200

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7698 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -1.4707 |
| sortino_ratio | -0.3896 |
| max_drawdown | 0.4298 |
| cagr | -0.1650 |
| net_avg_win | 72.8885 |
| net_avg_loss | -88.8390 |
| avg_hold_time_bars | 34.8319 |
| exposure | 0.5462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
