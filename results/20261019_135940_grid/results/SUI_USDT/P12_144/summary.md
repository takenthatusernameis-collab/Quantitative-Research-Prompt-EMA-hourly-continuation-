# EMA Hourly Continuation — SUI/USDT P12_144

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7258 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0215 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -2.1286 |
| sortino_ratio | -0.6382 |
| max_drawdown | 0.5416 |
| cagr | -0.2633 |
| net_avg_win | 62.4765 |
| net_avg_loss | -86.0819 |
| avg_hold_time_bars | 33.1167 |
| exposure | 0.6834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
