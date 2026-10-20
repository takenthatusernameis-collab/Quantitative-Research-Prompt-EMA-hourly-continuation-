# EMA Hourly Continuation — VELO/USDT P55_89

**Symbol:** VELO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -4.6061 |
| sortino_ratio | -1.7354 |
| max_drawdown | 0.8841 |
| cagr | -0.5650 |
| net_avg_win | 40.7424 |
| net_avg_loss | -60.9055 |
| avg_hold_time_bars | 4.1290 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
