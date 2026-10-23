# EMA Hourly Continuation — POKT/USDT P50_55

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 910 |
| net_profit_factor | 0.2861 |
| net_win_rate | 0.3209 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.3780 |
| sharpe_ratio | -12.9151 |
| sortino_ratio | -5.6415 |
| max_drawdown | 0.9995 |
| cagr | -0.9485 |
| net_avg_win | 13.7189 |
| net_avg_loss | -22.6542 |
| avg_hold_time_bars | 2.9780 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
