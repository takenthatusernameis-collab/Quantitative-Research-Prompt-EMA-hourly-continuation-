# EMA Hourly Continuation — FLIP/USDT P34_89

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.4488 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.7945 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -5.7173 |
| sortino_ratio | -1.7286 |
| max_drawdown | 0.8845 |
| cagr | -0.5730 |
| net_avg_win | 37.9923 |
| net_avg_loss | -58.6107 |
| avg_hold_time_bars | 11.8182 |
| exposure | 0.2482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
