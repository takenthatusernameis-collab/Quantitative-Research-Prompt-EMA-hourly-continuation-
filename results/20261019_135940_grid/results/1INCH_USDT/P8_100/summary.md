# EMA Hourly Continuation — 1INCH/USDT P8_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.5571 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8586 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -4.7526 |
| sortino_ratio | -1.6183 |
| max_drawdown | 0.8638 |
| cagr | -0.5397 |
| net_avg_win | 41.9739 |
| net_avg_loss | -59.2112 |
| avg_hold_time_bars | 26.4949 |
| exposure | 0.7033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
