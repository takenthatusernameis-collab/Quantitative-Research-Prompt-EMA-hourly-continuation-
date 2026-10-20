# EMA Hourly Continuation — BRETT/USDT P34_144

**Symbol:** BRETT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6656 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8513 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -2.6370 |
| sortino_ratio | -0.7758 |
| max_drawdown | 0.5820 |
| cagr | -0.3061 |
| net_avg_win | 60.4152 |
| net_avg_loss | -78.4507 |
| avg_hold_time_bars | 20.6917 |
| exposure | 0.4102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
