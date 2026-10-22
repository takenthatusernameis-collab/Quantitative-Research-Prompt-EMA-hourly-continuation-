# EMA Hourly Continuation — MOODENG/USDT P20_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7975 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -1.4545 |
| sortino_ratio | -0.4013 |
| max_drawdown | 0.3529 |
| cagr | -0.1701 |
| net_avg_win | 84.9662 |
| net_avg_loss | -97.9431 |
| avg_hold_time_bars | 32.5113 |
| exposure | 0.5559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
