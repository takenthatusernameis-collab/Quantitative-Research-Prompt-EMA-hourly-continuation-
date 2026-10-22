# EMA Hourly Continuation — ZKJ/USDT P21_89

**Symbol:** ZKJ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.1745 |
| net_win_rate | 0.2929 |
| gross_profit_factor | 0.4507 |
| gross_win_rate | 0.3535 |
| sharpe_ratio | -9.7485 |
| sortino_ratio | -2.9190 |
| max_drawdown | 0.9824 |
| cagr | -0.7975 |
| net_avg_win | 17.8906 |
| net_avg_loss | -42.4789 |
| avg_hold_time_bars | 42.6490 |
| exposure | 0.7677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
