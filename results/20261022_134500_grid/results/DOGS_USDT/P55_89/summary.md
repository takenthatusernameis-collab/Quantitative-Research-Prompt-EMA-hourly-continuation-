# EMA Hourly Continuation — DOGS/USDT P55_89

**Symbol:** DOGS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5689 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9288 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -5.2451 |
| sortino_ratio | -1.9610 |
| max_drawdown | 0.8715 |
| cagr | -0.6112 |
| net_avg_win | 40.9602 |
| net_avg_loss | -63.5924 |
| avg_hold_time_bars | 4.0988 |
| exposure | 0.1298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
