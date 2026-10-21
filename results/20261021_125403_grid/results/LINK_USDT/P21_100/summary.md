# EMA Hourly Continuation — LINK/USDT P21_100

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7175 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -2.4507 |
| sortino_ratio | -0.7255 |
| max_drawdown | 0.5912 |
| cagr | -0.2836 |
| net_avg_win | 71.6756 |
| net_avg_loss | -86.5472 |
| avg_hold_time_bars | 18.9400 |
| exposure | 0.3728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
