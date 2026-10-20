# EMA Hourly Continuation — UMA/USDT P50_200

**Symbol:** UMA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6526 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9863 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -2.8453 |
| sortino_ratio | -0.8591 |
| max_drawdown | 0.6437 |
| cagr | -0.3301 |
| net_avg_win | 53.9312 |
| net_avg_loss | -78.3811 |
| avg_hold_time_bars | 17.8678 |
| exposure | 0.3687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
