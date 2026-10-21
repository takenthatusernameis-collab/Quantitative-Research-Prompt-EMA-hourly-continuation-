# EMA Hourly Continuation — ARB/USDT P50_144

**Symbol:** ARB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7927 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.2700 |
| sortino_ratio | -0.3413 |
| max_drawdown | 0.3812 |
| cagr | -0.1462 |
| net_avg_win | 71.1957 |
| net_avg_loss | -89.8136 |
| avg_hold_time_bars | 16.1676 |
| exposure | 0.2587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
