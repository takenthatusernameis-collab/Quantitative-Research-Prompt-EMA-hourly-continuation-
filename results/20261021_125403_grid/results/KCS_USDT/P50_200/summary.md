# EMA Hourly Continuation — KCS/USDT P50_200

**Symbol:** KCS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.5973 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.6693 |
| sortino_ratio | -0.6300 |
| max_drawdown | 0.5158 |
| cagr | -0.2509 |
| net_avg_win | 58.8607 |
| net_avg_loss | -90.2137 |
| avg_hold_time_bars | 33.2132 |
| exposure | 0.4106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
