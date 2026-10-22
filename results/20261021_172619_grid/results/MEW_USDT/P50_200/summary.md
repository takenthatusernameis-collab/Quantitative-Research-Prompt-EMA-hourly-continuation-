# EMA Hourly Continuation — MEW/USDT P50_200

**Symbol:** MEW/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7673 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9041 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -1.3363 |
| sortino_ratio | -0.3105 |
| max_drawdown | 0.3458 |
| cagr | -0.1344 |
| net_avg_win | 78.9594 |
| net_avg_loss | -93.3501 |
| avg_hold_time_bars | 36.7940 |
| exposure | 0.4465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
