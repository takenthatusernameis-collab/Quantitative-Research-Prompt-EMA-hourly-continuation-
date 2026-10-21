# EMA Hourly Continuation — ZEN/USDT P21_26

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.6171 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.9200 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -2.2004 |
| sortino_ratio | -0.4425 |
| max_drawdown | 0.4034 |
| cagr | -0.1832 |
| net_avg_win | 69.0453 |
| net_avg_loss | -100.0509 |
| avg_hold_time_bars | 4.6650 |
| exposure | 0.0418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
