# EMA Hourly Continuation — INJ/USDT P21_50

**Symbol:** INJ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8766 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.1172 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -0.9269 |
| sortino_ratio | -0.2878 |
| max_drawdown | 0.3731 |
| cagr | -0.1264 |
| net_avg_win | 83.8190 |
| net_avg_loss | -106.5316 |
| avg_hold_time_bars | 7.2333 |
| exposure | 0.1522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
