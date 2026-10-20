# EMA Hourly Continuation — IOST/USDT P8_26

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1470 |
| net_profit_factor | 0.3880 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8755 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -10.0244 |
| sortino_ratio | -5.4398 |
| max_drawdown | 0.9989 |
| cagr | -0.9322 |
| net_avg_win | 9.6253 |
| net_avg_loss | -20.1008 |
| avg_hold_time_bars | 4.5014 |
| exposure | 0.3008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
