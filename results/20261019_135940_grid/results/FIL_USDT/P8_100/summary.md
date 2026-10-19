# EMA Hourly Continuation — FIL/USDT P8_100

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6182 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -3.7390 |
| sortino_ratio | -1.2605 |
| max_drawdown | 0.7936 |
| cagr | -0.4541 |
| net_avg_win | 46.6743 |
| net_avg_loss | -66.6503 |
| avg_hold_time_bars | 26.9100 |
| exposure | 0.7070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
