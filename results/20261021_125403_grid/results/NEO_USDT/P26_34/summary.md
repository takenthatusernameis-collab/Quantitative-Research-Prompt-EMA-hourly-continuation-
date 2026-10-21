# EMA Hourly Continuation — NEO/USDT P26_34

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.5050 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.7753 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -2.9925 |
| sortino_ratio | -0.6506 |
| max_drawdown | 0.5354 |
| cagr | -0.2575 |
| net_avg_win | 52.1449 |
| net_avg_loss | -83.7484 |
| avg_hold_time_bars | 5.2000 |
| exposure | 0.0544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
