# EMA Hourly Continuation — NEO/USDT P50_144

**Symbol:** NEO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6654 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8834 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.3039 |
| sortino_ratio | -0.6372 |
| max_drawdown | 0.5333 |
| cagr | -0.2531 |
| net_avg_win | 57.3892 |
| net_avg_loss | -79.2081 |
| avg_hold_time_bars | 15.4122 |
| exposure | 0.2634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
