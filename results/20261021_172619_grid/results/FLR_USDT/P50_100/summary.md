# EMA Hourly Continuation — FLR/USDT P50_100

**Symbol:** FLR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8460 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -2.8183 |
| sortino_ratio | -0.7825 |
| max_drawdown | 0.6000 |
| cagr | -0.3010 |
| net_avg_win | 51.8572 |
| net_avg_loss | -75.5502 |
| avg_hold_time_bars | 8.1724 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
