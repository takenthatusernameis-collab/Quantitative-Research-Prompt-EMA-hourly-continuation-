# EMA Hourly Continuation — SKY/USDT P20_26

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.2360 |
| net_win_rate | 0.3672 |
| gross_profit_factor | 0.7036 |
| gross_win_rate | 0.4349 |
| sharpe_ratio | -14.1228 |
| sortino_ratio | -7.0962 |
| max_drawdown | 0.9995 |
| cagr | -0.9768 |
| net_avg_win | 8.6263 |
| net_avg_loss | -21.2053 |
| avg_hold_time_bars | 2.2687 |
| exposure | 0.1233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
