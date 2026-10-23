# EMA Hourly Continuation — OGN/USDT P12_50

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.5906 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 1.0190 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -6.9590 |
| sortino_ratio | -3.1298 |
| max_drawdown | 0.9793 |
| cagr | -0.7810 |
| net_avg_win | 30.4800 |
| net_avg_loss | -42.4429 |
| avg_hold_time_bars | 7.5302 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
