# EMA Hourly Continuation — HTX/USDT P50_100

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.3811 |
| net_win_rate | 0.3553 |
| gross_profit_factor | 0.6580 |
| gross_win_rate | 0.3579 |
| sharpe_ratio | -7.0250 |
| sortino_ratio | -2.0244 |
| max_drawdown | 0.9140 |
| cagr | -0.6208 |
| net_avg_win | 40.1821 |
| net_avg_loss | -58.1076 |
| avg_hold_time_bars | 10.1675 |
| exposure | 0.1813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
