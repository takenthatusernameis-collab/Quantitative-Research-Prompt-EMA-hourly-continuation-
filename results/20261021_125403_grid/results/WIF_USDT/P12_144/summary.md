# EMA Hourly Continuation — WIF/USDT P12_144

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.8124 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9287 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -1.2647 |
| sortino_ratio | -0.3393 |
| max_drawdown | 0.3831 |
| cagr | -0.1466 |
| net_avg_win | 83.1813 |
| net_avg_loss | -95.1551 |
| avg_hold_time_bars | 40.4423 |
| exposure | 0.6526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
