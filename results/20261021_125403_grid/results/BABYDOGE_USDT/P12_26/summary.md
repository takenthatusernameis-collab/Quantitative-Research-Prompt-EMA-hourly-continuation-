# EMA Hourly Continuation — BABYDOGE/USDT P12_26

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 21 |
| net_profit_factor | 1.2080 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3239 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | 0.2813 |
| sortino_ratio | 0.0189 |
| max_drawdown | 0.0322 |
| cagr | 0.0077 |
| net_avg_win | 94.7142 |
| net_avg_loss | -104.5433 |
| avg_hold_time_bars | 7.2381 |
| exposure | 0.0069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
