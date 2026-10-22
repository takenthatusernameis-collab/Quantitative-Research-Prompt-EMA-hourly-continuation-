# EMA Hourly Continuation — REZ/USDT P50_55

**Symbol:** REZ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.9333 |
| net_win_rate | 0.5682 |
| gross_profit_factor | 1.3071 |
| gross_win_rate | 0.5682 |
| sharpe_ratio | -0.2641 |
| sortino_ratio | -0.0514 |
| max_drawdown | 0.2025 |
| cagr | -0.0255 |
| net_avg_win | 86.7552 |
| net_avg_loss | -122.3132 |
| avg_hold_time_bars | 5.6477 |
| exposure | 0.0459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
