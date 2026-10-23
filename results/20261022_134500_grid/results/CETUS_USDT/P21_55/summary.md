# EMA Hourly Continuation — CETUS/USDT P21_55

**Symbol:** CETUS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.5810 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -6.6458 |
| sortino_ratio | -2.8693 |
| max_drawdown | 0.9724 |
| cagr | -0.7521 |
| net_avg_win | 32.0307 |
| net_avg_loss | -43.6090 |
| avg_hold_time_bars | 5.2818 |
| exposure | 0.2273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
