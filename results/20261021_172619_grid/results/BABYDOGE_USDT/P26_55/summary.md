# EMA Hourly Continuation — BABYDOGE/USDT P26_55

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 27 |
| net_profit_factor | 1.1215 |
| net_win_rate | 0.5556 |
| gross_profit_factor | 1.2385 |
| gross_win_rate | 0.5556 |
| sharpe_ratio | 0.2028 |
| sortino_ratio | 0.0153 |
| max_drawdown | 0.0523 |
| cagr | 0.0061 |
| net_avg_win | 95.6116 |
| net_avg_loss | -106.5682 |
| avg_hold_time_bars | 16.3333 |
| exposure | 0.0200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
