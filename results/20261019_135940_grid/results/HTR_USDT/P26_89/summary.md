# EMA Hourly Continuation — HTR/USDT P26_89

**Symbol:** HTR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5168 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.7672 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -6.3800 |
| sortino_ratio | -2.4400 |
| max_drawdown | 0.9526 |
| cagr | -0.6995 |
| net_avg_win | 32.4977 |
| net_avg_loss | -45.3540 |
| avg_hold_time_bars | 9.2851 |
| exposure | 0.3153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
