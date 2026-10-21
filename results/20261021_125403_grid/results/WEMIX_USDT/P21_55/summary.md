# EMA Hourly Continuation — WEMIX/USDT P21_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.5524 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.7350 |
| gross_win_rate | 0.4125 |
| sharpe_ratio | -4.0050 |
| sortino_ratio | -1.1105 |
| max_drawdown | 0.7305 |
| cagr | -0.4026 |
| net_avg_win | 56.6954 |
| net_avg_loss | -72.0670 |
| avg_hold_time_bars | 12.8721 |
| exposure | 0.2241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
