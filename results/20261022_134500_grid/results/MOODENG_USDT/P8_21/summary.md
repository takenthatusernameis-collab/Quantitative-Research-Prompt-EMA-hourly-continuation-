# EMA Hourly Continuation — MOODENG/USDT P8_21

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1286 |
| net_profit_factor | 0.5617 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -9.8077 |
| sortino_ratio | -5.4322 |
| max_drawdown | 0.9966 |
| cagr | -0.9329 |
| net_avg_win | 22.8404 |
| net_avg_loss | -31.2652 |
| avg_hold_time_bars | 3.6081 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
