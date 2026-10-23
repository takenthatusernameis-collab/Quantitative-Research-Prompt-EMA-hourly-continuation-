# EMA Hourly Continuation — CHR/USDT P26_200

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7332 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.8567 |
| sortino_ratio | -0.4925 |
| max_drawdown | 0.4456 |
| cagr | -0.2046 |
| net_avg_win | 71.7720 |
| net_avg_loss | -90.8543 |
| avg_hold_time_bars | 39.8739 |
| exposure | 0.6297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
