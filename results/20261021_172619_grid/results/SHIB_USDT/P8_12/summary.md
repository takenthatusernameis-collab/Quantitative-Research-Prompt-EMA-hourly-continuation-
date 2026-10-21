# EMA Hourly Continuation — SHIB/USDT P8_12

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.7965 |
| net_win_rate | 0.5393 |
| gross_profit_factor | 1.1705 |
| gross_win_rate | 0.5393 |
| sharpe_ratio | -0.9874 |
| sortino_ratio | -0.1978 |
| max_drawdown | 0.2973 |
| cagr | -0.0864 |
| net_avg_win | 77.1521 |
| net_avg_loss | -113.3757 |
| avg_hold_time_bars | 4.6597 |
| exposure | 0.0405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
