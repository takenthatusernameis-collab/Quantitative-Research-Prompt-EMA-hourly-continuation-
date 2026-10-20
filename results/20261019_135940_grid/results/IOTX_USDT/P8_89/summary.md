# EMA Hourly Continuation — IOTX/USDT P8_89

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.5952 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -4.0312 |
| sortino_ratio | -1.3554 |
| max_drawdown | 0.8133 |
| cagr | -0.4769 |
| net_avg_win | 44.9211 |
| net_avg_loss | -64.6571 |
| avg_hold_time_bars | 27.5579 |
| exposure | 0.7140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
