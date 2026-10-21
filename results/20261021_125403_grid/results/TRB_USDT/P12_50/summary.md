# EMA Hourly Continuation — TRB/USDT P12_50

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -3.1497 |
| sortino_ratio | -1.1241 |
| max_drawdown | 0.7304 |
| cagr | -0.4025 |
| net_avg_win | 57.4643 |
| net_avg_loss | -71.7120 |
| avg_hold_time_bars | 10.9445 |
| exposure | 0.3125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
