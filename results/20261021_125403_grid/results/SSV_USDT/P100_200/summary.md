# EMA Hourly Continuation — SSV/USDT P100_200

**Symbol:** SSV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6406 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8174 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -2.4116 |
| sortino_ratio | -0.5932 |
| max_drawdown | 0.5165 |
| cagr | -0.2386 |
| net_avg_win | 65.1602 |
| net_avg_loss | -83.8406 |
| avg_hold_time_bars | 11.6080 |
| exposure | 0.1581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
