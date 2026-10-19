# EMA Hourly Continuation — ATOM/USDT P8_12

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1834 |
| net_profit_factor | 0.0997 |
| net_win_rate | 0.3375 |
| gross_profit_factor | 0.5673 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -19.9801 |
| sortino_ratio | -12.6078 |
| max_drawdown | 1.0000 |
| cagr | -0.9989 |
| net_avg_win | 1.7887 |
| net_avg_loss | -9.1417 |
| avg_hold_time_bars | 1.7034 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
