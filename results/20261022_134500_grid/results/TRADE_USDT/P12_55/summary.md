# EMA Hourly Continuation — TRADE/USDT P12_55

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.6208 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.9228 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -5.6348 |
| sortino_ratio | -2.3112 |
| max_drawdown | 0.9467 |
| cagr | -0.6822 |
| net_avg_win | 39.9342 |
| net_avg_loss | -51.8595 |
| avg_hold_time_bars | 9.3576 |
| exposure | 0.3688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
