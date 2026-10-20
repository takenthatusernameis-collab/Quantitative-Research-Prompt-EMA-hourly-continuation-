# EMA Hourly Continuation — EWT/USDT P12_55

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4265 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.7262 |
| gross_win_rate | 0.4259 |
| sharpe_ratio | -7.8320 |
| sortino_ratio | -3.3729 |
| max_drawdown | 0.9855 |
| cagr | -0.8145 |
| net_avg_win | 18.4140 |
| net_avg_loss | -31.0731 |
| avg_hold_time_bars | 7.1830 |
| exposure | 0.3105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
