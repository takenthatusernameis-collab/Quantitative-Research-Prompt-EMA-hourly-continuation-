# EMA Hourly Continuation — GRT/USDT P50_200

**Symbol:** GRT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.9521 |
| net_win_rate | 0.5399 |
| gross_profit_factor | 1.1531 |
| gross_win_rate | 0.5399 |
| sharpe_ratio | -0.1915 |
| sortino_ratio | -0.0448 |
| max_drawdown | 0.1332 |
| cagr | -0.0245 |
| net_avg_win | 84.8184 |
| net_avg_loss | -104.5429 |
| avg_hold_time_bars | 32.2548 |
| exposure | 0.3839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
