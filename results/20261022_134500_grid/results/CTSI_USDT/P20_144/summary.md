# EMA Hourly Continuation — CTSI/USDT P20_144

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.6428 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.9332 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -4.0760 |
| sortino_ratio | -1.3706 |
| max_drawdown | 0.8079 |
| cagr | -0.4760 |
| net_avg_win | 57.0953 |
| net_avg_loss | -71.5672 |
| avg_hold_time_bars | 20.3210 |
| exposure | 0.5237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
