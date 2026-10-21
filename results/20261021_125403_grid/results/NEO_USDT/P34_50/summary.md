# EMA Hourly Continuation — NEO/USDT P34_50

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.5693 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.8842 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -2.9286 |
| sortino_ratio | -0.7239 |
| max_drawdown | 0.5730 |
| cagr | -0.2804 |
| net_avg_win | 53.0972 |
| net_avg_loss | -83.6966 |
| avg_hold_time_bars | 5.3682 |
| exposure | 0.0722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
