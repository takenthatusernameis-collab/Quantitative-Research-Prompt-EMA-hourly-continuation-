# EMA Hourly Continuation — CFG/USDT P26_50

**Symbol:** CFG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 737 |
| net_profit_factor | 0.4124 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -6.5202 |
| sortino_ratio | -2.4878 |
| max_drawdown | 0.9545 |
| cagr | -0.7048 |
| net_avg_win | 21.0383 |
| net_avg_loss | -38.7193 |
| avg_hold_time_bars | 11.2157 |
| exposure | 0.3757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
