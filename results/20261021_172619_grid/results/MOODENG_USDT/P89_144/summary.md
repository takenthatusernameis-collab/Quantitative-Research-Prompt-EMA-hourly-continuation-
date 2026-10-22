# EMA Hourly Continuation — MOODENG/USDT P89_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.8766 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1091 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -0.6665 |
| sortino_ratio | -0.1654 |
| max_drawdown | 0.1713 |
| cagr | -0.0753 |
| net_avg_win | 82.7112 |
| net_avg_loss | -105.0236 |
| avg_hold_time_bars | 8.4198 |
| exposure | 0.1132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
