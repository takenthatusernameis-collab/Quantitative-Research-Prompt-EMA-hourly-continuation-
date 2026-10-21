# EMA Hourly Continuation — DOT/USDT P12_144

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.9814 |
| net_win_rate | 0.5442 |
| gross_profit_factor | 1.1806 |
| gross_win_rate | 0.5442 |
| sharpe_ratio | -0.0475 |
| sortino_ratio | -0.0118 |
| max_drawdown | 0.1807 |
| cagr | -0.0110 |
| net_avg_win | 89.7474 |
| net_avg_loss | -109.1973 |
| avg_hold_time_bars | 53.0476 |
| exposure | 0.7089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
