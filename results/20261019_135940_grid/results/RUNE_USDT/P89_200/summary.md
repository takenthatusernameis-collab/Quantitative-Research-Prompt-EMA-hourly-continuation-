# EMA Hourly Continuation — RUNE/USDT P89_200

**Symbol:** RUNE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7360 |
| net_win_rate | 0.5187 |
| gross_profit_factor | 1.0801 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -1.6530 |
| sortino_ratio | -0.4413 |
| max_drawdown | 0.4568 |
| cagr | -0.1842 |
| net_avg_win | 62.0075 |
| net_avg_loss | -90.8015 |
| avg_hold_time_bars | 11.7810 |
| exposure | 0.1858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
