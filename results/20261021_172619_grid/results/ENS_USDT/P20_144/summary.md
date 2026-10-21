# EMA Hourly Continuation — ENS/USDT P20_144

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7843 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.3461 |
| sortino_ratio | -0.3591 |
| max_drawdown | 0.4070 |
| cagr | -0.1535 |
| net_avg_win | 72.7123 |
| net_avg_loss | -89.0680 |
| avg_hold_time_bars | 36.6648 |
| exposure | 0.5816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
