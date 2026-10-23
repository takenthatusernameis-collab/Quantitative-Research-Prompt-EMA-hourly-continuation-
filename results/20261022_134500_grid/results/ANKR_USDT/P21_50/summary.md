# EMA Hourly Continuation — ANKR/USDT P21_50

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.5093 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -8.7024 |
| sortino_ratio | -3.8429 |
| max_drawdown | 0.9923 |
| cagr | -0.8537 |
| net_avg_win | 25.1136 |
| net_avg_loss | -35.4053 |
| avg_hold_time_bars | 6.2141 |
| exposure | 0.2771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
