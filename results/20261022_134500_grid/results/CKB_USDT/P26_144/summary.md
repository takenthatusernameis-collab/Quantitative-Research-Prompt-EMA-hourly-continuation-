# EMA Hourly Continuation — CKB/USDT P26_144

**Symbol:** CKB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9082 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -3.0353 |
| sortino_ratio | -0.9388 |
| max_drawdown | 0.6872 |
| cagr | -0.3614 |
| net_avg_win | 49.5483 |
| net_avg_loss | -73.5975 |
| avg_hold_time_bars | 22.5271 |
| exposure | 0.4915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
