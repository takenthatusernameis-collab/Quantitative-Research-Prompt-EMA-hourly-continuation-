# EMA Hourly Continuation — SATS/USDT P8_50

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.8165 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.8373 |
| sortino_ratio | -0.6856 |
| max_drawdown | 0.5691 |
| cagr | -0.2726 |
| net_avg_win | 72.2427 |
| net_avg_loss | -87.4502 |
| avg_hold_time_bars | 14.3070 |
| exposure | 0.4428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
