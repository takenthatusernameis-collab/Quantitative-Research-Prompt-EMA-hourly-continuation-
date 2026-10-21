# EMA Hourly Continuation — BNB/USDT P89_200

**Symbol:** BNB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.0792 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -2.0438 |
| sortino_ratio | -0.4914 |
| max_drawdown | 0.4336 |
| cagr | -0.1998 |
| net_avg_win | 53.3958 |
| net_avg_loss | -92.2274 |
| avg_hold_time_bars | 14.5560 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
