# EMA Hourly Continuation — MANA/USDT P21_55

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.5416 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -7.9221 |
| sortino_ratio | -3.4383 |
| max_drawdown | 0.9867 |
| cagr | -0.8170 |
| net_avg_win | 28.3417 |
| net_avg_loss | -40.3526 |
| avg_hold_time_bars | 5.4915 |
| exposure | 0.2356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
