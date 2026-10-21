# EMA Hourly Continuation — NEO/USDT P12_100

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7176 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9251 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.1976 |
| sortino_ratio | -0.6585 |
| max_drawdown | 0.5393 |
| cagr | -0.2608 |
| net_avg_win | 63.7384 |
| net_avg_loss | -82.2330 |
| avg_hold_time_bars | 29.6077 |
| exposure | 0.5935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
