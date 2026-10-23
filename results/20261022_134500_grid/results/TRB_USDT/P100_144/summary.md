# EMA Hourly Continuation — TRB/USDT P100_144

**Symbol:** TRB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.4219 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8265 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -5.5778 |
| sortino_ratio | -1.8131 |
| max_drawdown | 0.8952 |
| cagr | -0.5869 |
| net_avg_win | 27.1387 |
| net_avg_loss | -53.4193 |
| avg_hold_time_bars | 3.8355 |
| exposure | 0.0918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
