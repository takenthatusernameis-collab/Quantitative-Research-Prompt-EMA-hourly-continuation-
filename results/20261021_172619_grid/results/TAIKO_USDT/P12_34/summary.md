# EMA Hourly Continuation — TAIKO/USDT P12_34

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.8092 |
| net_win_rate | 0.5350 |
| gross_profit_factor | 1.1211 |
| gross_win_rate | 0.5350 |
| sharpe_ratio | -1.5784 |
| sortino_ratio | -0.5671 |
| max_drawdown | 0.5514 |
| cagr | -0.2295 |
| net_avg_win | 62.5601 |
| net_avg_loss | -88.9686 |
| avg_hold_time_bars | 7.4137 |
| exposure | 0.2083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
