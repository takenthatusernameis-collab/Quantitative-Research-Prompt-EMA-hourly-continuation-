# EMA Hourly Continuation — NEO/USDT P144_200

**Symbol:** NEO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.6038 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.3348 |
| sortino_ratio | -0.5101 |
| max_drawdown | 0.4548 |
| cagr | -0.2084 |
| net_avg_win | 61.4953 |
| net_avg_loss | -91.8363 |
| avg_hold_time_bars | 6.2112 |
| exposure | 0.0655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
