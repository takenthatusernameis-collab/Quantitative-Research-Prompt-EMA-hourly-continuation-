# EMA Hourly Continuation — LISTA/USDT P20_89

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -3.2926 |
| sortino_ratio | -1.2049 |
| max_drawdown | 0.7385 |
| cagr | -0.4339 |
| net_avg_win | 55.2598 |
| net_avg_loss | -73.5698 |
| avg_hold_time_bars | 13.3349 |
| exposure | 0.4088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
