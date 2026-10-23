# EMA Hourly Continuation — DUSK/USDT P34_55

**Symbol:** DUSK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 865 |
| net_profit_factor | 0.4610 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8533 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -7.2138 |
| sortino_ratio | -2.9888 |
| max_drawdown | 0.9760 |
| cagr | -0.7680 |
| net_avg_win | 22.1094 |
| net_avg_loss | -37.0498 |
| avg_hold_time_bars | 3.4462 |
| exposure | 0.1355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
