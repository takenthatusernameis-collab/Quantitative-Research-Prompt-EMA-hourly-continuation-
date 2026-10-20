# EMA Hourly Continuation — ID/USDT P21_50

**Symbol:** ID/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.5252 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9610 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -5.6853 |
| sortino_ratio | -2.3848 |
| max_drawdown | 0.9462 |
| cagr | -0.6832 |
| net_avg_win | 24.8885 |
| net_avg_loss | -42.4364 |
| avg_hold_time_bars | 5.6535 |
| exposure | 0.2275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
