# EMA Hourly Continuation — AKT/USDT P8_12

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.7396 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3731 |
| sortino_ratio | -0.2936 |
| max_drawdown | 0.2991 |
| cagr | -0.1258 |
| net_avg_win | 73.2959 |
| net_avg_loss | -99.1031 |
| avg_hold_time_bars | 5.0225 |
| exposure | 0.0507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
