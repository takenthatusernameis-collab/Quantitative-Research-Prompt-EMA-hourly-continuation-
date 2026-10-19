# EMA Hourly Continuation — AXS/USDT P89_144

**Symbol:** AXS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5507 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0486 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -3.8451 |
| sortino_ratio | -1.1392 |
| max_drawdown | 0.7661 |
| cagr | -0.4349 |
| net_avg_win | 41.3856 |
| net_avg_loss | -75.1498 |
| avg_hold_time_bars | 4.6681 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
