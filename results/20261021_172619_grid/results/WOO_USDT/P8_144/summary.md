# EMA Hourly Continuation — WOO/USDT P8_144

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8481 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.0529 |
| sortino_ratio | -0.2842 |
| max_drawdown | 0.3608 |
| cagr | -0.1243 |
| net_avg_win | 88.9328 |
| net_avg_loss | -104.2753 |
| avg_hold_time_bars | 47.2829 |
| exposure | 0.7673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
