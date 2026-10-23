# EMA Hourly Continuation — XPR/USDT P26_34

**Symbol:** XPR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.1647 |
| net_win_rate | 0.3133 |
| gross_profit_factor | 0.5100 |
| gross_win_rate | 0.3411 |
| sharpe_ratio | -14.8085 |
| sortino_ratio | -6.6760 |
| max_drawdown | 0.9999 |
| cagr | -0.9777 |
| net_avg_win | 6.9905 |
| net_avg_loss | -19.3699 |
| avg_hold_time_bars | 3.1656 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
