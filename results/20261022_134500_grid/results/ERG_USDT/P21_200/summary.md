# EMA Hourly Continuation — ERG/USDT P21_200

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.7842 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -3.8180 |
| sortino_ratio | -1.1532 |
| max_drawdown | 0.7605 |
| cagr | -0.4256 |
| net_avg_win | 43.5834 |
| net_avg_loss | -64.1748 |
| avg_hold_time_bars | 27.4082 |
| exposure | 0.5768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
