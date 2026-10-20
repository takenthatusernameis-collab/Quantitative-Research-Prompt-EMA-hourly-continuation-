# EMA Hourly Continuation — T/USDT P8_55

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.6368 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -4.8371 |
| sortino_ratio | -1.9590 |
| max_drawdown | 0.9075 |
| cagr | -0.6102 |
| net_avg_win | 40.0629 |
| net_avg_loss | -57.1542 |
| avg_hold_time_bars | 12.7146 |
| exposure | 0.4798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
