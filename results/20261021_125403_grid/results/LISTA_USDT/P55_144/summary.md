# EMA Hourly Continuation — LISTA/USDT P55_144

**Symbol:** LISTA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.7883 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9764 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.3834 |
| sortino_ratio | -0.3760 |
| max_drawdown | 0.3597 |
| cagr | -0.1600 |
| net_avg_win | 74.5864 |
| net_avg_loss | -93.4937 |
| avg_hold_time_bars | 17.3929 |
| exposure | 0.2858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
