# EMA Hourly Continuation — BLZ/USDT P89_200

**Symbol:** BLZ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6519 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.3909 |
| sortino_ratio | -1.0211 |
| max_drawdown | 0.7403 |
| cagr | -0.3840 |
| net_avg_win | 61.4528 |
| net_avg_loss | -83.4017 |
| avg_hold_time_bars | 12.6114 |
| exposure | 0.2614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
