# EMA Hourly Continuation — TFUEL/USDT P20_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6332 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.7836 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -3.2480 |
| sortino_ratio | -0.9432 |
| max_drawdown | 0.6777 |
| cagr | -0.3537 |
| net_avg_win | 62.9687 |
| net_avg_loss | -75.2005 |
| avg_hold_time_bars | 28.3671 |
| exposure | 0.5455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
