# EMA Hourly Continuation — BONK/USDT P26_34

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.8756 |
| net_win_rate | 0.5355 |
| gross_profit_factor | 1.1475 |
| gross_win_rate | 0.5355 |
| sharpe_ratio | -0.5089 |
| sortino_ratio | -0.0916 |
| max_drawdown | 0.2220 |
| cagr | -0.0424 |
| net_avg_win | 87.5582 |
| net_avg_loss | -115.2691 |
| avg_hold_time_bars | 4.6129 |
| exposure | 0.0325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
