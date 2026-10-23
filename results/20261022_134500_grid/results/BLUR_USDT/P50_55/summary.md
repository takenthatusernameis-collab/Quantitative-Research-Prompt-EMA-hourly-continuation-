# EMA Hourly Continuation — BLUR/USDT P50_55

**Symbol:** BLUR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 769 |
| net_profit_factor | 0.2672 |
| net_win_rate | 0.3914 |
| gross_profit_factor | 0.8388 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -10.5719 |
| sortino_ratio | -4.2221 |
| max_drawdown | 0.9968 |
| cagr | -0.8970 |
| net_avg_win | 12.0722 |
| net_avg_loss | -29.0628 |
| avg_hold_time_bars | 1.9168 |
| exposure | 0.0667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
