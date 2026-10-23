# EMA Hourly Continuation — BOSON/USDT P26_100

**Symbol:** BOSON/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6744 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -3.4391 |
| sortino_ratio | -1.2319 |
| max_drawdown | 0.7677 |
| cagr | -0.4404 |
| net_avg_win | 52.4581 |
| net_avg_loss | -68.7115 |
| avg_hold_time_bars | 11.6579 |
| exposure | 0.3423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
