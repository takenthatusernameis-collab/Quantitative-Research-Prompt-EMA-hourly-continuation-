# EMA Hourly Continuation — ARKM/USDT P8_20

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6705 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.9113 |
| sortino_ratio | -0.9425 |
| max_drawdown | 0.6707 |
| cagr | -0.3502 |
| net_avg_win | 55.8317 |
| net_avg_loss | -73.2400 |
| avg_hold_time_bars | 5.5650 |
| exposure | 0.1303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
