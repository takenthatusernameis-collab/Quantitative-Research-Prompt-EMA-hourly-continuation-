# EMA Hourly Continuation — DEGEN/USDT P20_21

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.3192 |
| net_win_rate | 0.3436 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.3996 |
| sharpe_ratio | -14.2862 |
| sortino_ratio | -6.9812 |
| max_drawdown | 0.9999 |
| cagr | -0.9788 |
| net_avg_win | 11.9626 |
| net_avg_loss | -19.6111 |
| avg_hold_time_bars | 2.0955 |
| exposure | 0.1089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
