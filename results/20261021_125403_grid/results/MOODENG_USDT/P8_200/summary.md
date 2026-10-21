# EMA Hourly Continuation — MOODENG/USDT P8_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 1.1283 |
| net_win_rate | 0.5622 |
| gross_profit_factor | 1.2784 |
| gross_win_rate | 0.5676 |
| sharpe_ratio | 0.6511 |
| sortino_ratio | 0.1426 |
| max_drawdown | 0.0946 |
| cagr | 0.0586 |
| net_avg_win | 105.4626 |
| net_avg_loss | -120.0078 |
| avg_hold_time_bars | 81.8216 |
| exposure | 0.8375 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
