# EMA Hourly Continuation — 1INCH/USDT P12_21

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.5672 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8589 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -3.3297 |
| sortino_ratio | -0.9364 |
| max_drawdown | 0.6628 |
| cagr | -0.3490 |
| net_avg_win | 47.7594 |
| net_avg_loss | -75.0830 |
| avg_hold_time_bars | 5.2812 |
| exposure | 0.0922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
