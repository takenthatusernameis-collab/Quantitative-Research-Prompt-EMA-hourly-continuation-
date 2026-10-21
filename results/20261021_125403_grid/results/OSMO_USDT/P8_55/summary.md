# EMA Hourly Continuation — OSMO/USDT P8_55

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.7935 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 1.0289 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -2.3357 |
| sortino_ratio | -0.8767 |
| max_drawdown | 0.7075 |
| cagr | -0.3320 |
| net_avg_win | 71.7774 |
| net_avg_loss | -88.8923 |
| avg_hold_time_bars | 15.7776 |
| exposure | 0.4934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
