# EMA Hourly Continuation — LINK/USDT P21_50

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.4628 |
| net_win_rate | 0.4223 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -8.5978 |
| sortino_ratio | -3.6498 |
| max_drawdown | 0.9899 |
| cagr | -0.8392 |
| net_avg_win | 22.2638 |
| net_avg_loss | -35.1630 |
| avg_hold_time_bars | 4.8765 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
