# EMA Hourly Continuation — ETC/USDT P55_144

**Symbol:** ETC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5244 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.3124 |
| sortino_ratio | -1.3842 |
| max_drawdown | 0.8147 |
| cagr | -0.4850 |
| net_avg_win | 36.0590 |
| net_avg_loss | -63.6329 |
| avg_hold_time_bars | 9.8857 |
| exposure | 0.2319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
