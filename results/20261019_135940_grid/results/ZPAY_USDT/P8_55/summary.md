# EMA Hourly Continuation — ZPAY/USDT P8_55

**Symbol:** ZPAY/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.4830 |
| net_win_rate | 0.3610 |
| gross_profit_factor | 0.6408 |
| gross_win_rate | 0.3610 |
| sharpe_ratio | -6.8165 |
| sortino_ratio | -2.5746 |
| max_drawdown | 0.9537 |
| cagr | -0.7029 |
| net_avg_win | 33.6024 |
| net_avg_loss | -39.3101 |
| avg_hold_time_bars | 15.2534 |
| exposure | 0.5066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
