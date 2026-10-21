# EMA Hourly Continuation — AURORA/USDT P8_21

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6382 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -4.3624 |
| sortino_ratio | -1.5179 |
| max_drawdown | 0.8398 |
| cagr | -0.5038 |
| net_avg_win | 52.5254 |
| net_avg_loss | -73.5749 |
| avg_hold_time_bars | 6.3633 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
