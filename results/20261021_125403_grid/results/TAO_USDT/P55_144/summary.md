# EMA Hourly Continuation — TAO/USDT P55_144

**Symbol:** TAO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.7882 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.2806 |
| sortino_ratio | -0.3177 |
| max_drawdown | 0.3127 |
| cagr | -0.1368 |
| net_avg_win | 78.1599 |
| net_avg_loss | -94.0500 |
| avg_hold_time_bars | 14.7550 |
| exposure | 0.2025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
