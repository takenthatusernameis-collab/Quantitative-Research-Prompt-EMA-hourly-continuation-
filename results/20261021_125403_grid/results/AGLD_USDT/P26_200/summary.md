# EMA Hourly Continuation — AGLD/USDT P26_200

**Symbol:** AGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7383 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -1.9730 |
| sortino_ratio | -0.5181 |
| max_drawdown | 0.5415 |
| cagr | -0.2122 |
| net_avg_win | 80.2263 |
| net_avg_loss | -93.3890 |
| avg_hold_time_bars | 37.2006 |
| exposure | 0.5791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
