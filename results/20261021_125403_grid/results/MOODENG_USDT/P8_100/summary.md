# EMA Hourly Continuation — MOODENG/USDT P8_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7941 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9303 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -1.6118 |
| sortino_ratio | -0.4874 |
| max_drawdown | 0.4164 |
| cagr | -0.2025 |
| net_avg_win | 80.8055 |
| net_avg_loss | -93.8507 |
| avg_hold_time_bars | 32.7817 |
| exposure | 0.6729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
