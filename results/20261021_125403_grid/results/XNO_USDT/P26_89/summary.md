# EMA Hourly Continuation — XNO/USDT P26_89

**Symbol:** XNO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6208 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.7813 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -3.4775 |
| sortino_ratio | -1.1026 |
| max_drawdown | 0.7320 |
| cagr | -0.3978 |
| net_avg_win | 54.0870 |
| net_avg_loss | -67.1109 |
| avg_hold_time_bars | 12.4691 |
| exposure | 0.2840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
