# EMA Hourly Continuation — CHR/USDT P21_34

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1117 |
| net_profit_factor | 0.3878 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.8548 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -9.7351 |
| sortino_ratio | -4.6076 |
| max_drawdown | 0.9969 |
| cagr | -0.8981 |
| net_avg_win | 13.6090 |
| net_avg_loss | -24.9358 |
| avg_hold_time_bars | 2.9427 |
| exposure | 0.1487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
