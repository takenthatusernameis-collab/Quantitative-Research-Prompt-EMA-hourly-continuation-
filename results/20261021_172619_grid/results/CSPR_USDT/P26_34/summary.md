# EMA Hourly Continuation — CSPR/USDT P26_34

**Symbol:** CSPR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.6148 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8267 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -2.2492 |
| sortino_ratio | -0.4341 |
| max_drawdown | 0.4346 |
| cagr | -0.1809 |
| net_avg_win | 77.6769 |
| net_avg_loss | -99.3601 |
| avg_hold_time_bars | 5.5163 |
| exposure | 0.0461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
