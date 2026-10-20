# EMA Hourly Continuation — NMR/USDT P8_144

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6789 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -2.8945 |
| sortino_ratio | -0.9628 |
| max_drawdown | 0.7021 |
| cagr | -0.3681 |
| net_avg_win | 53.5820 |
| net_avg_loss | -74.2501 |
| avg_hold_time_bars | 28.7199 |
| exposure | 0.7271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
