# EMA Hourly Continuation — MOG/USDT P55_89

**Symbol:** MOG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.6609 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -3.8789 |
| sortino_ratio | -1.4173 |
| max_drawdown | 0.7907 |
| cagr | -0.4826 |
| net_avg_win | 52.0484 |
| net_avg_loss | -74.4214 |
| avg_hold_time_bars | 3.8636 |
| exposure | 0.1154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
