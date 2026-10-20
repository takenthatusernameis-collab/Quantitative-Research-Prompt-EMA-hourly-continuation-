# EMA Hourly Continuation — OSMO/USDT P12_20

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1477 |
| net_profit_factor | 0.2980 |
| net_win_rate | 0.3731 |
| gross_profit_factor | 1.0017 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -14.9952 |
| sortino_ratio | -8.3068 |
| max_drawdown | 1.0000 |
| cagr | -0.9865 |
| net_avg_win | 7.7041 |
| net_avg_loss | -15.3831 |
| avg_hold_time_bars | 2.4882 |
| exposure | 0.1670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
