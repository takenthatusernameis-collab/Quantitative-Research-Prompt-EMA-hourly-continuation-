# EMA Hourly Continuation — BDX/USDT P20_100

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1208 |
| net_profit_factor | 0.3438 |
| net_win_rate | 0.3146 |
| gross_profit_factor | 0.7682 |
| gross_win_rate | 0.3560 |
| sharpe_ratio | -16.1803 |
| sortino_ratio | -8.2817 |
| max_drawdown | 1.0000 |
| cagr | -0.9893 |
| net_avg_win | 13.7861 |
| net_avg_loss | -18.4041 |
| avg_hold_time_bars | 5.9495 |
| exposure | 0.3267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
