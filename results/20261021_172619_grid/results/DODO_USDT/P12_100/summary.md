# EMA Hourly Continuation — DODO/USDT P12_100

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.7639 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9379 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.1832 |
| sortino_ratio | -0.7203 |
| max_drawdown | 0.6350 |
| cagr | -0.2826 |
| net_avg_win | 71.1724 |
| net_avg_loss | -85.5393 |
| avg_hold_time_bars | 21.3117 |
| exposure | 0.5198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
