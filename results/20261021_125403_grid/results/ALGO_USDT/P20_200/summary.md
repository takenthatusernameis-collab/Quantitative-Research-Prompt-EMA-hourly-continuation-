# EMA Hourly Continuation — ALGO/USDT P20_200

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.8781 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0355 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -0.6857 |
| sortino_ratio | -0.1716 |
| max_drawdown | 0.2694 |
| cagr | -0.0785 |
| net_avg_win | 85.7031 |
| net_avg_loss | -102.1858 |
| avg_hold_time_bars | 44.3016 |
| exposure | 0.6142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
