# EMA Hourly Continuation — BOME/USDT P55_89

**Symbol:** BOME/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.8556 |
| net_win_rate | 0.5240 |
| gross_profit_factor | 1.0863 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -0.8350 |
| sortino_ratio | -0.2200 |
| max_drawdown | 0.3070 |
| cagr | -0.0982 |
| net_avg_win | 77.3769 |
| net_avg_loss | -99.5365 |
| avg_hold_time_bars | 6.7246 |
| exposure | 0.1021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
