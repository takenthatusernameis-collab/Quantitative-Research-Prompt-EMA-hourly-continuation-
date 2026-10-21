# EMA Hourly Continuation — TRB/USDT P12_144

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6473 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.7836 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -2.5032 |
| sortino_ratio | -0.6753 |
| max_drawdown | 0.5706 |
| cagr | -0.2668 |
| net_avg_win | 61.5013 |
| net_avg_loss | -75.8200 |
| avg_hold_time_bars | 41.1370 |
| exposure | 0.6794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
