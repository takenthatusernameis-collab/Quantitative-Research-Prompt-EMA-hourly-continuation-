# EMA Hourly Continuation — FLUX/USDT P12_34

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0249 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.8554 |
| sortino_ratio | -0.6510 |
| max_drawdown | 0.6275 |
| cagr | -0.2585 |
| net_avg_win | 58.0356 |
| net_avg_loss | -79.2520 |
| avg_hold_time_bars | 6.2790 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
