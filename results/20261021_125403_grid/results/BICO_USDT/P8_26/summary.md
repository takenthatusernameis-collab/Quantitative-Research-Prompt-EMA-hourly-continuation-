# EMA Hourly Continuation — BICO/USDT P8_26

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 835 |
| net_profit_factor | 0.6883 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9253 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -3.3239 |
| sortino_ratio | -1.3726 |
| max_drawdown | 0.7973 |
| cagr | -0.4676 |
| net_avg_win | 43.5439 |
| net_avg_loss | -59.0155 |
| avg_hold_time_bars | 6.7928 |
| exposure | 0.2578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
