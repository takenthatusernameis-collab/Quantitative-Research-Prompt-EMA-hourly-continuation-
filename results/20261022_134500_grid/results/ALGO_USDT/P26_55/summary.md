# EMA Hourly Continuation — ALGO/USDT P26_55

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.5148 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -5.5380 |
| sortino_ratio | -2.3521 |
| max_drawdown | 0.9424 |
| cagr | -0.6747 |
| net_avg_win | 22.6232 |
| net_avg_loss | -42.7830 |
| avg_hold_time_bars | 4.0179 |
| exposure | 0.1633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
