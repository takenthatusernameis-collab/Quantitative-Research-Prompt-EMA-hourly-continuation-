# EMA Hourly Continuation — SOL/USDT P8_55

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1080 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -6.4791 |
| sortino_ratio | -2.9619 |
| max_drawdown | 0.9770 |
| cagr | -0.7726 |
| net_avg_win | 23.8089 |
| net_avg_loss | -38.9718 |
| avg_hold_time_bars | 8.9287 |
| exposure | 0.4383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
