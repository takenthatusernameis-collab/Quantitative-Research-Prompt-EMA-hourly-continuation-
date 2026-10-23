# EMA Hourly Continuation — CETUS/USDT P8_144

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.9170 |
| net_win_rate | 0.5529 |
| gross_profit_factor | 1.2485 |
| gross_win_rate | 0.5576 |
| sharpe_ratio | -0.5231 |
| sortino_ratio | -0.1533 |
| max_drawdown | 0.3425 |
| cagr | -0.0751 |
| net_avg_win | 84.0671 |
| net_avg_loss | -113.3860 |
| avg_hold_time_bars | 40.5765 |
| exposure | 0.7804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
