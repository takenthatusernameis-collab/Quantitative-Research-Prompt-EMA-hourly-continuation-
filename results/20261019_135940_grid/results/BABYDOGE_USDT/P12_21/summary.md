# EMA Hourly Continuation — BABYDOGE/USDT P12_21

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 19 |
| net_profit_factor | 0.8112 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8892 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -0.2706 |
| sortino_ratio | -0.0167 |
| max_drawdown | 0.0373 |
| cagr | -0.0078 |
| net_avg_win | 93.3307 |
| net_avg_loss | -103.5523 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
