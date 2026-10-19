# EMA Hourly Continuation — NEO/USDT P12_50

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1054 |
| net_profit_factor | 0.4436 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.8342 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -8.0794 |
| sortino_ratio | -3.7134 |
| max_drawdown | 0.9890 |
| cagr | -0.8342 |
| net_avg_win | 17.3273 |
| net_avg_loss | -29.6733 |
| avg_hold_time_bars | 7.5332 |
| exposure | 0.3609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
