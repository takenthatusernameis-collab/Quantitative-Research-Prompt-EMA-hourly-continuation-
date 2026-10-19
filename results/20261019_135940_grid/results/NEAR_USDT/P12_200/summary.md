# EMA Hourly Continuation — NEAR/USDT P12_200

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.8302 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0511 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.0985 |
| sortino_ratio | -0.2802 |
| max_drawdown | 0.4269 |
| cagr | -0.1239 |
| net_avg_win | 85.3069 |
| net_avg_loss | -104.6940 |
| avg_hold_time_bars | 52.1776 |
| exposure | 0.7613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
