# EMA Hourly Continuation — CTSI/USDT P21_144

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.6292 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.9257 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -4.2385 |
| sortino_ratio | -1.4038 |
| max_drawdown | 0.8162 |
| cagr | -0.4851 |
| net_avg_win | 56.8869 |
| net_avg_loss | -70.8049 |
| avg_hold_time_bars | 21.3938 |
| exposure | 0.5358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
