# EMA Hourly Continuation — BSV/USDT P50_100

**Symbol:** BSV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6016 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8529 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.2314 |
| sortino_ratio | -0.9218 |
| max_drawdown | 0.6602 |
| cagr | -0.3447 |
| net_avg_win | 53.9835 |
| net_avg_loss | -76.0185 |
| avg_hold_time_bars | 9.5865 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
