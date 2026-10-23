# EMA Hourly Continuation — IOTX/USDT P26_200

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6754 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9405 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -2.3714 |
| sortino_ratio | -0.6977 |
| max_drawdown | 0.5703 |
| cagr | -0.2797 |
| net_avg_win | 55.6164 |
| net_avg_loss | -77.1951 |
| avg_hold_time_bars | 27.8272 |
| exposure | 0.5490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
