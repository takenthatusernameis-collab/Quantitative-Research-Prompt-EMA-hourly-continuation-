# EMA Hourly Continuation — IOST/USDT P20_200

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7712 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.1126 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -1.6045 |
| sortino_ratio | -0.4458 |
| max_drawdown | 0.4645 |
| cagr | -0.1926 |
| net_avg_win | 69.7015 |
| net_avg_loss | -97.6652 |
| avg_hold_time_bars | 36.1654 |
| exposure | 0.6362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
