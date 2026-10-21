# EMA Hourly Continuation — DBR/USDT P34_50

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.4863 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8577 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -3.5861 |
| sortino_ratio | -0.8460 |
| max_drawdown | 0.5653 |
| cagr | -0.3286 |
| net_avg_win | 52.6533 |
| net_avg_loss | -89.3199 |
| avg_hold_time_bars | 9.0274 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
