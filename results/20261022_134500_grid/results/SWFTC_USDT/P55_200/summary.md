# EMA Hourly Continuation — SWFTC/USDT P55_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.5623 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -4.4578 |
| sortino_ratio | -1.3263 |
| max_drawdown | 0.8109 |
| cagr | -0.4760 |
| net_avg_win | 53.4378 |
| net_avg_loss | -71.6417 |
| avg_hold_time_bars | 14.9911 |
| exposure | 0.3060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
