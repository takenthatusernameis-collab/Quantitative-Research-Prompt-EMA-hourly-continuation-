# EMA Hourly Continuation — SUI/USDT P55_200

**Symbol:** SUI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6462 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9135 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.6689 |
| sortino_ratio | -0.7564 |
| max_drawdown | 0.6169 |
| cagr | -0.3010 |
| net_avg_win | 55.8424 |
| net_avg_loss | -80.5996 |
| avg_hold_time_bars | 18.2736 |
| exposure | 0.3339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
