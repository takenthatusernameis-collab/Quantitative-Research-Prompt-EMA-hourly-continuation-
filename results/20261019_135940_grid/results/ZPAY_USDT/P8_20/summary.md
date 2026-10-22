# EMA Hourly Continuation — ZPAY/USDT P8_20

**Symbol:** ZPAY/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1130 |
| net_profit_factor | 0.3665 |
| net_win_rate | 0.3301 |
| gross_profit_factor | 0.6263 |
| gross_win_rate | 0.3389 |
| sharpe_ratio | -10.7674 |
| sortino_ratio | -5.0562 |
| max_drawdown | 0.9978 |
| cagr | -0.9109 |
| net_avg_win | 15.4765 |
| net_avg_loss | -20.8062 |
| avg_hold_time_bars | 5.9655 |
| exposure | 0.3050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
