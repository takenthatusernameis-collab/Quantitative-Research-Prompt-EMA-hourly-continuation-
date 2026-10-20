# EMA Hourly Continuation — DOGS/USDT P21_144

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7854 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0677 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -1.7629 |
| sortino_ratio | -0.5681 |
| max_drawdown | 0.4803 |
| cagr | -0.2370 |
| net_avg_win | 70.5182 |
| net_avg_loss | -96.0771 |
| avg_hold_time_bars | 22.7991 |
| exposure | 0.5358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
