# EMA Hourly Continuation — YFI/USDT P8_34

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1512 |
| net_profit_factor | 0.3642 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -11.3193 |
| sortino_ratio | -6.1757 |
| max_drawdown | 0.9997 |
| cagr | -0.9573 |
| net_avg_win | 8.7033 |
| net_avg_loss | -18.4113 |
| avg_hold_time_bars | 5.2037 |
| exposure | 0.3560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
