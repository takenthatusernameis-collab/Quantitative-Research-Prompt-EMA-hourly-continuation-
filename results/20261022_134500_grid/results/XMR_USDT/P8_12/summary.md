# EMA Hourly Continuation — XMR/USDT P8_12

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2063 |
| net_profit_factor | 0.0903 |
| net_win_rate | 0.3054 |
| gross_profit_factor | 0.4271 |
| gross_win_rate | 0.3446 |
| sharpe_ratio | -23.2737 |
| sortino_ratio | -15.7255 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 1.5749 |
| net_avg_loss | -7.6707 |
| avg_hold_time_bars | 1.4954 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
