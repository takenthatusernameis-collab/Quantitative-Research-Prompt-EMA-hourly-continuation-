# EMA Hourly Continuation — ONDO/USDT P50_89

**Symbol:** ONDO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.8019 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -2.6617 |
| sortino_ratio | -0.6531 |
| max_drawdown | 0.5482 |
| cagr | -0.2591 |
| net_avg_win | 67.7269 |
| net_avg_loss | -84.3070 |
| avg_hold_time_bars | 8.2709 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
