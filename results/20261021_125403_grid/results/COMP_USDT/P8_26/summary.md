# EMA Hourly Continuation — COMP/USDT P8_26

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8556 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -4.6362 |
| sortino_ratio | -1.8689 |
| max_drawdown | 0.8883 |
| cagr | -0.5764 |
| net_avg_win | 35.1812 |
| net_avg_loss | -51.3537 |
| avg_hold_time_bars | 6.4748 |
| exposure | 0.2337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
