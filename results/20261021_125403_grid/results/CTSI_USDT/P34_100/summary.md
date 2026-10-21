# EMA Hourly Continuation — CTSI/USDT P34_100

**Symbol:** CTSI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.6902 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.9367 |
| sortino_ratio | -0.9586 |
| max_drawdown | 0.6812 |
| cagr | -0.3560 |
| net_avg_win | 60.8062 |
| net_avg_loss | -77.0914 |
| avg_hold_time_bars | 11.5257 |
| exposure | 0.2750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
