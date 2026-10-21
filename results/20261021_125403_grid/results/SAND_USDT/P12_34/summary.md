# EMA Hourly Continuation — SAND/USDT P12_34

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7124 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.6050 |
| sortino_ratio | -0.8907 |
| max_drawdown | 0.6471 |
| cagr | -0.3350 |
| net_avg_win | 56.7051 |
| net_avg_loss | -77.1212 |
| avg_hold_time_bars | 6.8612 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
