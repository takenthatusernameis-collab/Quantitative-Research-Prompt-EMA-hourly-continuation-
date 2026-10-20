# EMA Hourly Continuation — RSR/USDT P21_89

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6913 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -3.4874 |
| sortino_ratio | -1.2852 |
| max_drawdown | 0.8084 |
| cagr | -0.4577 |
| net_avg_win | 53.2593 |
| net_avg_loss | -72.0241 |
| avg_hold_time_bars | 11.9517 |
| exposure | 0.3710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
