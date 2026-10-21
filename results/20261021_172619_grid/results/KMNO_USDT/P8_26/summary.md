# EMA Hourly Continuation — KMNO/USDT P8_26

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.7771 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0481 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -2.0542 |
| sortino_ratio | -0.7698 |
| max_drawdown | 0.5904 |
| cagr | -0.3003 |
| net_avg_win | 59.2451 |
| net_avg_loss | -80.4390 |
| avg_hold_time_bars | 6.7842 |
| exposure | 0.2105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
