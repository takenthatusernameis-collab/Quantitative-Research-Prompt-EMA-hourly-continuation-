# EMA Hourly Continuation — ALGO/USDT P20_50

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7810 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0579 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.6473 |
| sortino_ratio | -0.5230 |
| max_drawdown | 0.4745 |
| cagr | -0.2132 |
| net_avg_win | 64.2802 |
| net_avg_loss | -87.9073 |
| avg_hold_time_bars | 7.0864 |
| exposure | 0.1565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
