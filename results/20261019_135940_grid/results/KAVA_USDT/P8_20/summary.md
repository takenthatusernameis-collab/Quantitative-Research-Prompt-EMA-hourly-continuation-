# EMA Hourly Continuation — KAVA/USDT P8_20

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1774 |
| net_profit_factor | 0.2643 |
| net_win_rate | 0.3890 |
| gross_profit_factor | 0.7076 |
| gross_win_rate | 0.4369 |
| sharpe_ratio | -15.4302 |
| sortino_ratio | -9.2769 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 5.2054 |
| net_avg_loss | -12.5384 |
| avg_hold_time_bars | 3.1888 |
| exposure | 0.2571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
