# EMA Hourly Continuation — PUNDIX/USDT P12_20

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.4751 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7653 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -5.5016 |
| sortino_ratio | -1.7988 |
| max_drawdown | 0.8796 |
| cagr | -0.5648 |
| net_avg_win | 35.7260 |
| net_avg_loss | -56.3974 |
| avg_hold_time_bars | 5.6390 |
| exposure | 0.1328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
