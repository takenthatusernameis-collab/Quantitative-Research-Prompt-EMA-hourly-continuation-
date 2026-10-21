# EMA Hourly Continuation — MAGIC/USDT P12_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 1.0040 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -1.6490 |
| sortino_ratio | -0.5299 |
| max_drawdown | 0.5258 |
| cagr | -0.2178 |
| net_avg_win | 81.0025 |
| net_avg_loss | -97.7857 |
| avg_hold_time_bars | 25.1304 |
| exposure | 0.5780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
