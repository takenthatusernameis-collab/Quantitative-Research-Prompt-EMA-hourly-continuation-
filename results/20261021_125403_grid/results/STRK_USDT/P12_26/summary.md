# EMA Hourly Continuation — STRK/USDT P12_26

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7859 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0308 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -1.3143 |
| sortino_ratio | -0.3859 |
| max_drawdown | 0.4300 |
| cagr | -0.1634 |
| net_avg_win | 61.6537 |
| net_avg_loss | -83.9165 |
| avg_hold_time_bars | 5.4856 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
