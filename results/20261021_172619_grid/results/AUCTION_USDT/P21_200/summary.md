# EMA Hourly Continuation — AUCTION/USDT P21_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6728 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -2.4209 |
| sortino_ratio | -0.6523 |
| max_drawdown | 0.5461 |
| cagr | -0.2622 |
| net_avg_win | 65.1657 |
| net_avg_loss | -83.5115 |
| avg_hold_time_bars | 36.8274 |
| exposure | 0.6084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
