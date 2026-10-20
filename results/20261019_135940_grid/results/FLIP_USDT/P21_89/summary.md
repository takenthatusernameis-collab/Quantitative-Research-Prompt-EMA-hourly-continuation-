# EMA Hourly Continuation — FLIP/USDT P21_89

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.4814 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -5.1179 |
| sortino_ratio | -1.5951 |
| max_drawdown | 0.8629 |
| cagr | -0.5420 |
| net_avg_win | 37.9896 |
| net_avg_loss | -58.1433 |
| avg_hold_time_bars | 19.0303 |
| exposure | 0.4282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
