# EMA Hourly Continuation — LPT/USDT P89_144

**Symbol:** LPT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7826 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0503 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.2840 |
| sortino_ratio | -0.3185 |
| max_drawdown | 0.3443 |
| cagr | -0.1362 |
| net_avg_win | 72.3672 |
| net_avg_loss | -98.2513 |
| avg_hold_time_bars | 7.7980 |
| exposure | 0.1053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
