# EMA Hourly Continuation — YGG/USDT P34_144

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.8600 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0413 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -0.9475 |
| sortino_ratio | -0.2657 |
| max_drawdown | 0.3317 |
| cagr | -0.1176 |
| net_avg_win | 84.8394 |
| net_avg_loss | -102.8442 |
| avg_hold_time_bars | 23.0833 |
| exposure | 0.4011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
