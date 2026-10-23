# EMA Hourly Continuation — EDU/USDT P8_55

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1052 |
| net_profit_factor | 0.5736 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8428 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -5.4170 |
| sortino_ratio | -2.4733 |
| max_drawdown | 0.9499 |
| cagr | -0.6909 |
| net_avg_win | 26.4625 |
| net_avg_loss | -39.0132 |
| avg_hold_time_bars | 10.7804 |
| exposure | 0.5132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
