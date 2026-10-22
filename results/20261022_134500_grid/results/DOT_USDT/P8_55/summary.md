# EMA Hourly Continuation — DOT/USDT P8_55

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9990 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -5.4182 |
| sortino_ratio | -2.3304 |
| max_drawdown | 0.9470 |
| cagr | -0.6808 |
| net_avg_win | 28.5105 |
| net_avg_loss | -45.5368 |
| avg_hold_time_bars | 12.2513 |
| exposure | 0.5274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
