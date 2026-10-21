# EMA Hourly Continuation — XDC/USDT P8_100

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.7834 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0956 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -1.8672 |
| sortino_ratio | -0.6307 |
| max_drawdown | 0.5332 |
| cagr | -0.2508 |
| net_avg_win | 65.4399 |
| net_avg_loss | -88.8324 |
| avg_hold_time_bars | 21.1826 |
| exposure | 0.5325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
