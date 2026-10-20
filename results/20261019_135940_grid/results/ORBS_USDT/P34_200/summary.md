# EMA Hourly Continuation — ORBS/USDT P34_200

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6124 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -4.2045 |
| sortino_ratio | -1.2676 |
| max_drawdown | 0.7965 |
| cagr | -0.4649 |
| net_avg_win | 60.1555 |
| net_avg_loss | -78.2838 |
| avg_hold_time_bars | 22.9339 |
| exposure | 0.4889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
