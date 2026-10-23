# EMA Hourly Continuation — POKT/USDT P34_200

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6160 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8401 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -3.9916 |
| sortino_ratio | -1.2579 |
| max_drawdown | 0.7799 |
| cagr | -0.4466 |
| net_avg_win | 57.5623 |
| net_avg_loss | -70.8273 |
| avg_hold_time_bars | 23.2236 |
| exposure | 0.5265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
