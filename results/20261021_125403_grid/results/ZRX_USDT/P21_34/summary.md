# EMA Hourly Continuation — ZRX/USDT P21_34

**Symbol:** ZRX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.5681 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8799 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -3.8602 |
| sortino_ratio | -1.2042 |
| max_drawdown | 0.7551 |
| cagr | -0.4250 |
| net_avg_win | 44.2936 |
| net_avg_loss | -69.8240 |
| avg_hold_time_bars | 4.9915 |
| exposure | 0.1071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
