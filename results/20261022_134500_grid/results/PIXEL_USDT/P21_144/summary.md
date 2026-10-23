# EMA Hourly Continuation — PIXEL/USDT P21_144

**Symbol:** PIXEL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7850 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0419 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -1.7894 |
| sortino_ratio | -0.5493 |
| max_drawdown | 0.5653 |
| cagr | -0.2310 |
| net_avg_win | 73.3898 |
| net_avg_loss | -96.7040 |
| avg_hold_time_bars | 25.6835 |
| exposure | 0.5509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
