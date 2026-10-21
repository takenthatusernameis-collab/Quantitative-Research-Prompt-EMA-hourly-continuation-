# EMA Hourly Continuation — AVAX/USDT P21_89

**Symbol:** AVAX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7925 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.8066 |
| sortino_ratio | -0.5529 |
| max_drawdown | 0.5215 |
| cagr | -0.2250 |
| net_avg_win | 79.5256 |
| net_avg_loss | -98.6146 |
| avg_hold_time_bars | 15.7511 |
| exposure | 0.3279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
