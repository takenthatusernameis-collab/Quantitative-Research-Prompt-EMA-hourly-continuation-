# EMA Hourly Continuation — AURORA/USDT P20_55

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8457 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -3.8287 |
| sortino_ratio | -1.1700 |
| max_drawdown | 0.7576 |
| cagr | -0.4198 |
| net_avg_win | 51.4227 |
| net_avg_loss | -71.7282 |
| avg_hold_time_bars | 10.9631 |
| exposure | 0.2297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
