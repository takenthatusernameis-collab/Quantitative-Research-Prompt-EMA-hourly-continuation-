# EMA Hourly Continuation — MEME/USDT P12_200

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8731 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0297 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -0.7602 |
| sortino_ratio | -0.1917 |
| max_drawdown | 0.3360 |
| cagr | -0.0866 |
| net_avg_win | 88.5907 |
| net_avg_loss | -105.4701 |
| avg_hold_time_bars | 52.2129 |
| exposure | 0.7357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
