# EMA Hourly Continuation — BABYDOGE/USDT P8_144

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 90 |
| net_profit_factor | 0.9804 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0362 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -0.0320 |
| sortino_ratio | -0.0043 |
| max_drawdown | 0.1166 |
| cagr | -0.0037 |
| net_avg_win | 100.9939 |
| net_avg_loss | -107.6926 |
| avg_hold_time_bars | 75.2667 |
| exposure | 0.3065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
