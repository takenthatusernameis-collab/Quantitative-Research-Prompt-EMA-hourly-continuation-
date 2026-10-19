# EMA Hourly Continuation — HBAR/USDT P89_144

**Symbol:** HBAR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5685 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 1.0546 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -4.7112 |
| sortino_ratio | -1.5001 |
| max_drawdown | 0.8533 |
| cagr | -0.5266 |
| net_avg_win | 45.5613 |
| net_avg_loss | -72.4480 |
| avg_hold_time_bars | 4.9225 |
| exposure | 0.1155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
