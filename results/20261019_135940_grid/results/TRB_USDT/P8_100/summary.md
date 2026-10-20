# EMA Hourly Continuation — TRB/USDT P8_100

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.5157 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8082 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -5.1648 |
| sortino_ratio | -1.8214 |
| max_drawdown | 0.8955 |
| cagr | -0.5881 |
| net_avg_win | 33.9746 |
| net_avg_loss | -51.3802 |
| avg_hold_time_bars | 23.7011 |
| exposure | 0.6853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
