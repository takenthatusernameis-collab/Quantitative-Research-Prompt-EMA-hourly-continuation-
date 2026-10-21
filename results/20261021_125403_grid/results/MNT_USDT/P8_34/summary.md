# EMA Hourly Continuation — MNT/USDT P8_34

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.6468 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9209 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -3.9010 |
| sortino_ratio | -1.5449 |
| max_drawdown | 0.8365 |
| cagr | -0.5086 |
| net_avg_win | 41.5226 |
| net_avg_loss | -58.7519 |
| avg_hold_time_bars | 9.6523 |
| exposure | 0.3370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
