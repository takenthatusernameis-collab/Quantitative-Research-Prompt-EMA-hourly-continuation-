# EMA Hourly Continuation — BCH/USDT P8_144

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.8359 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -1.0206 |
| sortino_ratio | -0.2510 |
| max_drawdown | 0.3332 |
| cagr | -0.1107 |
| net_avg_win | 86.0442 |
| net_avg_loss | -107.9415 |
| avg_hold_time_bars | 58.2373 |
| exposure | 0.7809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
