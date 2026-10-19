# EMA Hourly Continuation — MANA/USDT P89_144

**Symbol:** MANA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.4538 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -5.9314 |
| sortino_ratio | -1.9319 |
| max_drawdown | 0.9181 |
| cagr | -0.6231 |
| net_avg_win | 31.4954 |
| net_avg_loss | -56.7055 |
| avg_hold_time_bars | 4.2631 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
