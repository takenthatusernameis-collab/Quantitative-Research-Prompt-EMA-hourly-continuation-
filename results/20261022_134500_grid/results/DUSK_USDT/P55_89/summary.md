# EMA Hourly Continuation — DUSK/USDT P55_89

**Symbol:** DUSK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5149 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -5.2482 |
| sortino_ratio | -1.9447 |
| max_drawdown | 0.9075 |
| cagr | -0.6111 |
| net_avg_win | 30.0705 |
| net_avg_loss | -49.9719 |
| avg_hold_time_bars | 4.1052 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
