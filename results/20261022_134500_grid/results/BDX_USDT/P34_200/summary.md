# EMA Hourly Continuation — BDX/USDT P34_200

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.3736 |
| net_win_rate | 0.3352 |
| gross_profit_factor | 0.7843 |
| gross_win_rate | 0.3898 |
| sharpe_ratio | -12.4180 |
| sortino_ratio | -5.3652 |
| max_drawdown | 0.9994 |
| cagr | -0.9453 |
| net_avg_win | 19.8029 |
| net_avg_loss | -26.7234 |
| avg_hold_time_bars | 9.0535 |
| exposure | 0.3695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
