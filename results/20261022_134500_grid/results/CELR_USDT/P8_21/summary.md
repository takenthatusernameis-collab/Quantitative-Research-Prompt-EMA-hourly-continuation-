# EMA Hourly Continuation — CELR/USDT P8_21

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1591 |
| net_profit_factor | 0.3664 |
| net_win_rate | 0.4224 |
| gross_profit_factor | 0.8596 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -11.2242 |
| sortino_ratio | -6.3151 |
| max_drawdown | 0.9996 |
| cagr | -0.9555 |
| net_avg_win | 8.6021 |
| net_avg_loss | -17.1673 |
| avg_hold_time_bars | 3.4978 |
| exposure | 0.2518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
