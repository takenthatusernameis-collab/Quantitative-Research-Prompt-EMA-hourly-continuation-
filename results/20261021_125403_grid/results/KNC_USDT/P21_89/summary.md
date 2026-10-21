# EMA Hourly Continuation — KNC/USDT P21_89

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7482 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 1.0134 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.6714 |
| sortino_ratio | -0.8767 |
| max_drawdown | 0.7023 |
| cagr | -0.3318 |
| net_avg_win | 73.5970 |
| net_avg_loss | -93.6330 |
| avg_hold_time_bars | 16.4345 |
| exposure | 0.3937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
