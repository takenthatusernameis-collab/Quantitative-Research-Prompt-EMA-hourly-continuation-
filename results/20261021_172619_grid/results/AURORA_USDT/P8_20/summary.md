# EMA Hourly Continuation — AURORA/USDT P8_20

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.6093 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -4.5452 |
| sortino_ratio | -1.5621 |
| max_drawdown | 0.8466 |
| cagr | -0.5152 |
| net_avg_win | 48.5592 |
| net_avg_loss | -70.0621 |
| avg_hold_time_bars | 6.1113 |
| exposure | 0.1597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
