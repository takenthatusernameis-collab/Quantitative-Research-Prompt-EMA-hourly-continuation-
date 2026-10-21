# EMA Hourly Continuation — RAY/USDT P21_89

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.8344 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0176 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.2423 |
| sortino_ratio | -0.3897 |
| max_drawdown | 0.4469 |
| cagr | -0.1660 |
| net_avg_win | 76.2383 |
| net_avg_loss | -93.2974 |
| avg_hold_time_bars | 14.7035 |
| exposure | 0.3201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
