# EMA Hourly Continuation — SATS/USDT P34_100

**Symbol:** SATS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7333 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9196 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -2.1520 |
| sortino_ratio | -0.6238 |
| max_drawdown | 0.5562 |
| cagr | -0.2498 |
| net_avg_win | 71.9599 |
| net_avg_loss | -88.2783 |
| avg_hold_time_bars | 12.9447 |
| exposure | 0.2437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
