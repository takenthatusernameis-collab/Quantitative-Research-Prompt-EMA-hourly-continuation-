# EMA Hourly Continuation — NEO/USDT P89_200

**Symbol:** NEO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6665 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8941 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -2.0847 |
| sortino_ratio | -0.5133 |
| max_drawdown | 0.4541 |
| cagr | -0.2108 |
| net_avg_win | 63.0897 |
| net_avg_loss | -86.7170 |
| avg_hold_time_bars | 12.9899 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
