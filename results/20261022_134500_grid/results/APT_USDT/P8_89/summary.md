# EMA Hourly Continuation — APT/USDT P8_89

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9783 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -3.5505 |
| sortino_ratio | -1.2719 |
| max_drawdown | 0.8017 |
| cagr | -0.4610 |
| net_avg_win | 49.5577 |
| net_avg_loss | -70.1521 |
| avg_hold_time_bars | 22.0076 |
| exposure | 0.6552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
