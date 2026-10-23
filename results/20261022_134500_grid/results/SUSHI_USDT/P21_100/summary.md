# EMA Hourly Continuation — SUSHI/USDT P21_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.6202 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9446 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -4.5008 |
| sortino_ratio | -1.6382 |
| max_drawdown | 0.8721 |
| cagr | -0.5505 |
| net_avg_win | 44.9368 |
| net_avg_loss | -62.5333 |
| avg_hold_time_bars | 13.6868 |
| exposure | 0.4212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
