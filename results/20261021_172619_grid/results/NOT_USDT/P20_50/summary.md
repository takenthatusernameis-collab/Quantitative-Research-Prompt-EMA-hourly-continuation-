# EMA Hourly Continuation — NOT/USDT P20_50

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8223 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -1.2607 |
| sortino_ratio | -0.3961 |
| max_drawdown | 0.4158 |
| cagr | -0.1677 |
| net_avg_win | 69.9745 |
| net_avg_loss | -90.8173 |
| avg_hold_time_bars | 7.1063 |
| exposure | 0.1539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
