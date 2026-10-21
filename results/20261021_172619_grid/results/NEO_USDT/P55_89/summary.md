# EMA Hourly Continuation — NEO/USDT P55_89

**Symbol:** NEO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.4844 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.7126 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -3.5834 |
| sortino_ratio | -0.9176 |
| max_drawdown | 0.6747 |
| cagr | -0.3456 |
| net_avg_win | 43.6568 |
| net_avg_loss | -70.2126 |
| avg_hold_time_bars | 6.4161 |
| exposure | 0.0939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
