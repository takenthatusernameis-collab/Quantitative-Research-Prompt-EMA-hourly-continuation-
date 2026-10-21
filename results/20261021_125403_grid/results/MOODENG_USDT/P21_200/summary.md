# EMA Hourly Continuation — MOODENG/USDT P21_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.8455 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.7876 |
| sortino_ratio | -0.1679 |
| max_drawdown | 0.2035 |
| cagr | -0.0761 |
| net_avg_win | 90.5816 |
| net_avg_loss | -104.8359 |
| avg_hold_time_bars | 69.5978 |
| exposure | 0.7086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
