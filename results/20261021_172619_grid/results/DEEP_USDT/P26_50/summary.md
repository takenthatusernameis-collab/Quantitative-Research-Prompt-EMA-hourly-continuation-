# EMA Hourly Continuation — DEEP/USDT P26_50

**Symbol:** DEEP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.8890 |
| net_win_rate | 0.5307 |
| gross_profit_factor | 1.1211 |
| gross_win_rate | 0.5307 |
| sharpe_ratio | -0.6866 |
| sortino_ratio | -0.1943 |
| max_drawdown | 0.2206 |
| cagr | -0.0888 |
| net_avg_win | 83.4288 |
| net_avg_loss | -106.1456 |
| avg_hold_time_bars | 6.4595 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
