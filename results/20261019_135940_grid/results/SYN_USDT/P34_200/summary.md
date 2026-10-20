# EMA Hourly Continuation — SYN/USDT P34_200

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8407 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1075 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.9444 |
| sortino_ratio | -0.2614 |
| max_drawdown | 0.3271 |
| cagr | -0.1171 |
| net_avg_win | 71.9520 |
| net_avg_loss | -95.2524 |
| avg_hold_time_bars | 31.8904 |
| exposure | 0.5421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
