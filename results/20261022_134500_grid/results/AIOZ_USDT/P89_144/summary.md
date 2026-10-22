# EMA Hourly Continuation — AIOZ/USDT P89_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.5517 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -4.8486 |
| sortino_ratio | -1.6005 |
| max_drawdown | 0.8691 |
| cagr | -0.5422 |
| net_avg_win | 42.1321 |
| net_avg_loss | -64.1111 |
| avg_hold_time_bars | 4.4400 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
