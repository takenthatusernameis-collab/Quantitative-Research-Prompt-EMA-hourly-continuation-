# EMA Hourly Continuation — NEAR/USDT P50_89

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.4856 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -5.5096 |
| sortino_ratio | -1.9589 |
| max_drawdown | 0.9158 |
| cagr | -0.6238 |
| net_avg_win | 29.2526 |
| net_avg_loss | -50.9202 |
| avg_hold_time_bars | 4.1102 |
| exposure | 0.1203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
