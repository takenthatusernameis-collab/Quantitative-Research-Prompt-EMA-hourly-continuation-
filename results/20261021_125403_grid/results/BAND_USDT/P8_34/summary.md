# EMA Hourly Continuation — BAND/USDT P8_34

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.7646 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0483 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -2.9750 |
| sortino_ratio | -1.2475 |
| max_drawdown | 0.7697 |
| cagr | -0.4354 |
| net_avg_win | 57.5349 |
| net_avg_loss | -75.7775 |
| avg_hold_time_bars | 8.5902 |
| exposure | 0.3339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
