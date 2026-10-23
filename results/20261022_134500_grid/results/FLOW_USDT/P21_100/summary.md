# EMA Hourly Continuation — FLOW/USDT P21_100

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5477 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8615 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -4.9140 |
| sortino_ratio | -1.7410 |
| max_drawdown | 0.8828 |
| cagr | -0.5687 |
| net_avg_win | 37.6069 |
| net_avg_loss | -55.2073 |
| avg_hold_time_bars | 15.2866 |
| exposure | 0.4412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
