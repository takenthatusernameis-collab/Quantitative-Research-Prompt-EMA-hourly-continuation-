# EMA Hourly Continuation — SAND/USDT P26_50

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6295 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -2.8536 |
| sortino_ratio | -0.7906 |
| max_drawdown | 0.6348 |
| cagr | -0.3032 |
| net_avg_win | 57.5543 |
| net_avg_loss | -80.8673 |
| avg_hold_time_bars | 7.2853 |
| exposure | 0.1242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
