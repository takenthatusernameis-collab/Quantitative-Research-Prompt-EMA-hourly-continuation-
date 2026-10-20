# EMA Hourly Continuation — CELO/USDT P21_200

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7789 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0834 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.6188 |
| sortino_ratio | -0.4402 |
| max_drawdown | 0.4568 |
| cagr | -0.1861 |
| net_avg_win | 77.5702 |
| net_avg_loss | -100.1330 |
| avg_hold_time_bars | 38.3079 |
| exposure | 0.6362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
