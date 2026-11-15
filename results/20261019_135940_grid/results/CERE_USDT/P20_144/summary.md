# EMA Hourly Continuation — CERE/USDT P20_144

**Symbol:** CERE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.4680 |
| net_win_rate | 0.3720 |
| gross_profit_factor | 0.7213 |
| gross_win_rate | 0.3959 |
| sharpe_ratio | -7.1381 |
| sortino_ratio | -2.4363 |
| max_drawdown | 0.9586 |
| cagr | -0.7040 |
| net_avg_win | 38.4620 |
| net_avg_loss | -48.6813 |
| avg_hold_time_bars | 20.3584 |
| exposure | 0.5423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
