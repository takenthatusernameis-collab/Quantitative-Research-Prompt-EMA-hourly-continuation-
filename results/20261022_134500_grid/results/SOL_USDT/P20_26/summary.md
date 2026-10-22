# EMA Hourly Continuation — SOL/USDT P20_26

**Symbol:** SOL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1121 |
| net_profit_factor | 0.1787 |
| net_win_rate | 0.3310 |
| gross_profit_factor | 0.6255 |
| gross_win_rate | 0.3925 |
| sharpe_ratio | -15.6427 |
| sortino_ratio | -7.7801 |
| max_drawdown | 1.0000 |
| cagr | -0.9862 |
| net_avg_win | 5.8655 |
| net_avg_loss | -16.2345 |
| avg_hold_time_bars | 1.9019 |
| exposure | 0.0969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
