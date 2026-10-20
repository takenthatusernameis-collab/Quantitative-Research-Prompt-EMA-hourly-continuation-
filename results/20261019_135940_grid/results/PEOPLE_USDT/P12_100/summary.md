# EMA Hourly Continuation — PEOPLE/USDT P12_100

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -3.6461 |
| sortino_ratio | -1.2272 |
| max_drawdown | 0.7848 |
| cagr | -0.4417 |
| net_avg_win | 52.0903 |
| net_avg_loss | -67.7759 |
| avg_hold_time_bars | 23.3518 |
| exposure | 0.6097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
