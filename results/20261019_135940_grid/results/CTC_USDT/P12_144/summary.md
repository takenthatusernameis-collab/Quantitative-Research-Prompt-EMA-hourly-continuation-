# EMA Hourly Continuation — CTC/USDT P12_144

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6644 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -2.9713 |
| sortino_ratio | -0.9596 |
| max_drawdown | 0.7292 |
| cagr | -0.3754 |
| net_avg_win | 51.9868 |
| net_avg_loss | -76.2264 |
| avg_hold_time_bars | 27.5252 |
| exposure | 0.6694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
