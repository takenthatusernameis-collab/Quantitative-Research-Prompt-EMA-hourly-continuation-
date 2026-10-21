# EMA Hourly Continuation — NEO/USDT P8_89

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7248 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9260 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -2.0740 |
| sortino_ratio | -0.6458 |
| max_drawdown | 0.5505 |
| cagr | -0.2579 |
| net_avg_win | 59.8532 |
| net_avg_loss | -78.1970 |
| avg_hold_time_bars | 30.5094 |
| exposure | 0.6615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
