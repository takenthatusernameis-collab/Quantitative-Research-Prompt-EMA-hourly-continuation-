# EMA Hourly Continuation — BAT/USDT P21_89

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7818 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0470 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.9468 |
| sortino_ratio | -0.6543 |
| max_drawdown | 0.5962 |
| cagr | -0.2596 |
| net_avg_win | 68.2991 |
| net_avg_loss | -89.6150 |
| avg_hold_time_bars | 15.1239 |
| exposure | 0.3774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
