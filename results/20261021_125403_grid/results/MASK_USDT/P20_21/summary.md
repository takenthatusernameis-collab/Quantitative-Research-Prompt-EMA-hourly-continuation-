# EMA Hourly Continuation — MASK/USDT P20_21

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6068 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.4147 |
| sortino_ratio | -0.5321 |
| max_drawdown | 0.4860 |
| cagr | -0.2172 |
| net_avg_win | 61.1185 |
| net_avg_loss | -98.1758 |
| avg_hold_time_bars | 6.0340 |
| exposure | 0.0645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
