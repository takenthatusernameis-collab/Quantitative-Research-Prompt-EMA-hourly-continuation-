# EMA Hourly Continuation — W/USDT P20_144

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7969 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0893 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -1.8051 |
| sortino_ratio | -0.5762 |
| max_drawdown | 0.5765 |
| cagr | -0.2406 |
| net_avg_win | 75.2853 |
| net_avg_loss | -97.8655 |
| avg_hold_time_bars | 23.3620 |
| exposure | 0.5426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
