# EMA Hourly Continuation — IOTA/USDT P89_200

**Symbol:** IOTA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.8201 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0437 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -0.9855 |
| sortino_ratio | -0.2256 |
| max_drawdown | 0.3250 |
| cagr | -0.0997 |
| net_avg_win | 81.2700 |
| net_avg_loss | -103.8924 |
| avg_hold_time_bars | 16.5354 |
| exposure | 0.1909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
