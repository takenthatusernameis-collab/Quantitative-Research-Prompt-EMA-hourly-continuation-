# EMA Hourly Continuation — FLR/USDT P26_50

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1139 |
| net_profit_factor | 0.3655 |
| net_win_rate | 0.3916 |
| gross_profit_factor | 0.8450 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -11.7966 |
| sortino_ratio | -5.6813 |
| max_drawdown | 0.9994 |
| cagr | -0.9456 |
| net_avg_win | 12.9084 |
| net_avg_loss | -22.7279 |
| avg_hold_time_bars | 3.5119 |
| exposure | 0.1818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
