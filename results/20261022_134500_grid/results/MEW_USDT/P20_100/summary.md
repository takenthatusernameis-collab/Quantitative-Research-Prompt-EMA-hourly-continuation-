# EMA Hourly Continuation — MEW/USDT P20_100

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6049 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.9826 |
| sortino_ratio | -1.4143 |
| max_drawdown | 0.8344 |
| cagr | -0.4994 |
| net_avg_win | 41.3590 |
| net_avg_loss | -60.2740 |
| avg_hold_time_bars | 14.4071 |
| exposure | 0.4263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
