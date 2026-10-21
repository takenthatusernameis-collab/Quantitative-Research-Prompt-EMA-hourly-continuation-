# EMA Hourly Continuation — AAVE/USDT P21_26

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.6725 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -1.4684 |
| sortino_ratio | -0.2379 |
| max_drawdown | 0.2790 |
| cagr | -0.1034 |
| net_avg_win | 80.7057 |
| net_avg_loss | -109.2673 |
| avg_hold_time_bars | 6.1484 |
| exposure | 0.0358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
