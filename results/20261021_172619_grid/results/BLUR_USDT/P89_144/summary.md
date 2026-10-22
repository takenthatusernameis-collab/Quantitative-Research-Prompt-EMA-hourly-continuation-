# EMA Hourly Continuation — BLUR/USDT P89_144

**Symbol:** BLUR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.7888 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0713 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -1.3293 |
| sortino_ratio | -0.3388 |
| max_drawdown | 0.3522 |
| cagr | -0.1448 |
| net_avg_win | 74.7222 |
| net_avg_loss | -101.5787 |
| avg_hold_time_bars | 7.5111 |
| exposure | 0.1071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
