# EMA Hourly Continuation — NEO/USDT P34_144

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6659 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -2.1504 |
| sortino_ratio | -0.5995 |
| max_drawdown | 0.5585 |
| cagr | -0.2402 |
| net_avg_win | 54.5797 |
| net_avg_loss | -74.5872 |
| avg_hold_time_bars | 22.6990 |
| exposure | 0.3941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
