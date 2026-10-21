# EMA Hourly Continuation — FLOKI/USDT P100_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.7673 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -1.1965 |
| sortino_ratio | -0.2626 |
| max_drawdown | 0.2855 |
| cagr | -0.1136 |
| net_avg_win | 72.4129 |
| net_avg_loss | -98.5079 |
| avg_hold_time_bars | 7.3691 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
