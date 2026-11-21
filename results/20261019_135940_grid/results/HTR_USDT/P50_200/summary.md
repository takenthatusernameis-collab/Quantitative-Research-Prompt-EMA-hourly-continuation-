# EMA Hourly Continuation — HTR/USDT P50_200

**Symbol:** HTR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.5404 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -4.9006 |
| sortino_ratio | -1.5548 |
| max_drawdown | 0.8698 |
| cagr | -0.5415 |
| net_avg_win | 45.2873 |
| net_avg_loss | -62.0875 |
| avg_hold_time_bars | 14.6031 |
| exposure | 0.3478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
