# EMA Hourly Continuation — TNSR/USDT P34_55

**Symbol:** TNSR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6679 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9124 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.5446 |
| sortino_ratio | -0.7022 |
| max_drawdown | 0.5716 |
| cagr | -0.2750 |
| net_avg_win | 62.4248 |
| net_avg_loss | -85.3562 |
| avg_hold_time_bars | 6.1120 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
