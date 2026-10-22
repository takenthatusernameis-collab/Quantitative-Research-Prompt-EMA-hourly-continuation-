# EMA Hourly Continuation — ZPAY/USDT P50_144

**Symbol:** ZPAY/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.4717 |
| net_win_rate | 0.3694 |
| gross_profit_factor | 0.6143 |
| gross_win_rate | 0.3713 |
| sharpe_ratio | -5.2410 |
| sortino_ratio | -1.6527 |
| max_drawdown | 0.8588 |
| cagr | -0.5380 |
| net_avg_win | 40.7204 |
| net_avg_loss | -50.5610 |
| avg_hold_time_bars | 17.1002 |
| exposure | 0.3939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
