# EMA Hourly Continuation — AURORA/USDT P12_50

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -4.0411 |
| sortino_ratio | -1.3750 |
| max_drawdown | 0.8072 |
| cagr | -0.4718 |
| net_avg_win | 48.4921 |
| net_avg_loss | -65.0731 |
| avg_hold_time_bars | 12.2705 |
| exposure | 0.3196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
