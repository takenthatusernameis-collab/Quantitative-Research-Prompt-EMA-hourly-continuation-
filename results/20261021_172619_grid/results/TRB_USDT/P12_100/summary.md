# EMA Hourly Continuation — TRB/USDT P12_100

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7120 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -2.2961 |
| sortino_ratio | -0.7172 |
| max_drawdown | 0.5817 |
| cagr | -0.2805 |
| net_avg_win | 61.1666 |
| net_avg_loss | -76.5148 |
| avg_hold_time_bars | 24.9339 |
| exposure | 0.5461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
