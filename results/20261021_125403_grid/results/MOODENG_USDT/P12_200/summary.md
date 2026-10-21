# EMA Hourly Continuation — MOODENG/USDT P12_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 1.0031 |
| net_win_rate | 0.5317 |
| gross_profit_factor | 1.1350 |
| gross_win_rate | 0.5366 |
| sharpe_ratio | 0.0663 |
| sortino_ratio | 0.0151 |
| max_drawdown | 0.1482 |
| cagr | 0.0016 |
| net_avg_win | 100.6105 |
| net_avg_loss | -113.8812 |
| avg_hold_time_bars | 69.3171 |
| exposure | 0.7863 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
