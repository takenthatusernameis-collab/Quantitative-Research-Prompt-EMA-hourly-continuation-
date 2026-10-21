# EMA Hourly Continuation — OP/USDT P12_20

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.8264 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1460 |
| gross_win_rate | 0.5362 |
| sharpe_ratio | -0.9502 |
| sortino_ratio | -0.2285 |
| max_drawdown | 0.2967 |
| cagr | -0.1001 |
| net_avg_win | 74.8132 |
| net_avg_loss | -104.6757 |
| avg_hold_time_bars | 5.0435 |
| exposure | 0.0633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
