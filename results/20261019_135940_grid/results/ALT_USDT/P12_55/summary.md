# EMA Hourly Continuation — ALT/USDT P12_55

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.9070 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.0896 |
| sortino_ratio | -2.1413 |
| max_drawdown | 0.9260 |
| cagr | -0.6376 |
| net_avg_win | 37.4935 |
| net_avg_loss | -50.4709 |
| avg_hold_time_bars | 9.6087 |
| exposure | 0.3896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
