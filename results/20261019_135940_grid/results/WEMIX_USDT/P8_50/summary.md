# EMA Hourly Continuation — WEMIX/USDT P8_50

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1613 |
| net_profit_factor | 0.2458 |
| net_win_rate | 0.3100 |
| gross_profit_factor | 0.4636 |
| gross_win_rate | 0.3267 |
| sharpe_ratio | -16.5504 |
| sortino_ratio | -9.4714 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 6.5193 |
| net_avg_loss | -11.9134 |
| avg_hold_time_bars | 6.4247 |
| exposure | 0.4710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
