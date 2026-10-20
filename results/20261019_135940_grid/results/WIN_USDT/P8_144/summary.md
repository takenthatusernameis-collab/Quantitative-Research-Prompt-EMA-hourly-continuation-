# EMA Hourly Continuation — WIN/USDT P8_144

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5299 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8553 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -3.9247 |
| sortino_ratio | -1.2029 |
| max_drawdown | 0.7823 |
| cagr | -0.4505 |
| net_avg_win | 38.9632 |
| net_avg_loss | -63.6296 |
| avg_hold_time_bars | 33.7134 |
| exposure | 0.7432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
