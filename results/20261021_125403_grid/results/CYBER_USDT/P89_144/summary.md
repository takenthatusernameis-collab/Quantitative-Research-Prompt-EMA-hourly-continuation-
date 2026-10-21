# EMA Hourly Continuation — CYBER/USDT P89_144

**Symbol:** CYBER/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.0595 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -1.1836 |
| sortino_ratio | -0.2950 |
| max_drawdown | 0.3728 |
| cagr | -0.1267 |
| net_avg_win | 65.6921 |
| net_avg_loss | -91.8285 |
| avg_hold_time_bars | 8.4716 |
| exposure | 0.1151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
