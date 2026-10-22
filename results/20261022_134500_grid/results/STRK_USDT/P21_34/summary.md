# EMA Hourly Continuation — STRK/USDT P21_34

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.3684 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.7867 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -9.4410 |
| sortino_ratio | -4.4685 |
| max_drawdown | 0.9963 |
| cagr | -0.8908 |
| net_avg_win | 12.2329 |
| net_avg_loss | -24.7601 |
| avg_hold_time_bars | 2.5486 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
