# EMA Hourly Continuation — AMP/USDT P20_34

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.4007 |
| net_win_rate | 0.3582 |
| gross_profit_factor | 0.5965 |
| gross_win_rate | 0.3582 |
| sharpe_ratio | -5.8930 |
| sortino_ratio | -1.6588 |
| max_drawdown | 0.8614 |
| cagr | -0.5387 |
| net_avg_win | 41.2119 |
| net_avg_loss | -57.4120 |
| avg_hold_time_bars | 5.1521 |
| exposure | 0.0909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
