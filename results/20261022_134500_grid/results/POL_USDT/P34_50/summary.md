# EMA Hourly Continuation — POL/USDT P34_50

**Symbol:** POL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.2374 |
| net_win_rate | 0.3921 |
| gross_profit_factor | 0.6099 |
| gross_win_rate | 0.4274 |
| sharpe_ratio | -11.2308 |
| sortino_ratio | -5.0872 |
| max_drawdown | 0.9985 |
| cagr | -0.9254 |
| net_avg_win | 7.9895 |
| net_avg_loss | -21.7134 |
| avg_hold_time_bars | 2.7157 |
| exposure | 0.1225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
