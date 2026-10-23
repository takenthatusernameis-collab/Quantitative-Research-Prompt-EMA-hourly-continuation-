# EMA Hourly Continuation — XYO/USDT P26_144

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.4641 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.7948 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -6.5905 |
| sortino_ratio | -2.3211 |
| max_drawdown | 0.9478 |
| cagr | -0.6855 |
| net_avg_win | 31.3889 |
| net_avg_loss | -47.1983 |
| avg_hold_time_bars | 15.2205 |
| exposure | 0.4374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
