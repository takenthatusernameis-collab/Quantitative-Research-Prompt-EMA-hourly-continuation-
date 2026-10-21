# EMA Hourly Continuation — ANKR/USDT P20_50

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8698 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -4.2275 |
| sortino_ratio | -1.4577 |
| max_drawdown | 0.8203 |
| cagr | -0.4897 |
| net_avg_win | 51.3196 |
| net_avg_loss | -67.2380 |
| avg_hold_time_bars | 9.4205 |
| exposure | 0.2505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
