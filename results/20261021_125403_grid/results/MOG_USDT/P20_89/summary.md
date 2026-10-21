# EMA Hourly Continuation — MOG/USDT P20_89

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.8309 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -1.2593 |
| sortino_ratio | -0.3873 |
| max_drawdown | 0.4137 |
| cagr | -0.1651 |
| net_avg_win | 79.3490 |
| net_avg_loss | -94.1569 |
| avg_hold_time_bars | 17.7896 |
| exposure | 0.3741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
