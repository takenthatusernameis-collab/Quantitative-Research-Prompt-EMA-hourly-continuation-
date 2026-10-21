# EMA Hourly Continuation — DUSK/USDT P50_89

**Symbol:** DUSK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7535 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9661 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -1.7416 |
| sortino_ratio | -0.5043 |
| max_drawdown | 0.4552 |
| cagr | -0.2071 |
| net_avg_win | 66.8393 |
| net_avg_loss | -86.5647 |
| avg_hold_time_bars | 6.6479 |
| exposure | 0.1236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
