# EMA Hourly Continuation — VR/USDT P20_21

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 142 |
| net_profit_factor | 0.5873 |
| net_win_rate | 0.4366 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -2.2396 |
| sortino_ratio | -0.3767 |
| max_drawdown | 0.4091 |
| cagr | -0.1642 |
| net_avg_win | 83.2271 |
| net_avg_loss | -109.8214 |
| avg_hold_time_bars | 6.8732 |
| exposure | 0.0444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
