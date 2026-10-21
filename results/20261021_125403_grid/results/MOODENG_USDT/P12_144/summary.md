# EMA Hourly Continuation — MOODENG/USDT P12_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.9410 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0718 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -0.2966 |
| sortino_ratio | -0.0754 |
| max_drawdown | 0.1621 |
| cagr | -0.0385 |
| net_avg_win | 93.3444 |
| net_avg_loss | -106.3924 |
| avg_hold_time_bars | 51.1051 |
| exposure | 0.7267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
