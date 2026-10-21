# EMA Hourly Continuation — RUNE/USDT P12_34

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6788 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9303 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -3.2134 |
| sortino_ratio | -1.0916 |
| max_drawdown | 0.7226 |
| cagr | -0.3937 |
| net_avg_win | 56.1925 |
| net_avg_loss | -75.2363 |
| avg_hold_time_bars | 7.4885 |
| exposure | 0.1923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
