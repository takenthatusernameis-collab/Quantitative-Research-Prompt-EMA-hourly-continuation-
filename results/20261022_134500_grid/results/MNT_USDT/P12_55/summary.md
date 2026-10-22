# EMA Hourly Continuation — MNT/USDT P12_55

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.3613 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.7149 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -7.7887 |
| sortino_ratio | -3.2744 |
| max_drawdown | 0.9857 |
| cagr | -0.8145 |
| net_avg_win | 13.9701 |
| net_avg_loss | -30.0167 |
| avg_hold_time_bars | 9.8335 |
| exposure | 0.4081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
