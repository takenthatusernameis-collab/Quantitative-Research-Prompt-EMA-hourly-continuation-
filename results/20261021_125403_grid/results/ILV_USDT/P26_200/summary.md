# EMA Hourly Continuation — ILV/USDT P26_200

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.9947 |
| net_win_rate | 0.5482 |
| gross_profit_factor | 1.1939 |
| gross_win_rate | 0.5482 |
| sharpe_ratio | 0.0260 |
| sortino_ratio | 0.0065 |
| max_drawdown | 0.1098 |
| cagr | -0.0031 |
| net_avg_win | 89.8506 |
| net_avg_loss | -109.5884 |
| avg_hold_time_bars | 43.2359 |
| exposure | 0.5915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
