# EMA Hourly Continuation — SHIB/USDT P8_200

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6653 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -2.8355 |
| sortino_ratio | -0.8126 |
| max_drawdown | 0.6363 |
| cagr | -0.3267 |
| net_avg_win | 59.8808 |
| net_avg_loss | -88.7334 |
| avg_hold_time_bars | 40.7601 |
| exposure | 0.7800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
