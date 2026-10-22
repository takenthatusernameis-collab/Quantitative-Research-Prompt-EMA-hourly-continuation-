# EMA Hourly Continuation — DIA/USDT P8_26

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 771 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9291 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -3.3465 |
| sortino_ratio | -1.3275 |
| max_drawdown | 0.7838 |
| cagr | -0.4551 |
| net_avg_win | 43.2508 |
| net_avg_loss | -60.7501 |
| avg_hold_time_bars | 6.6978 |
| exposure | 0.2337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
