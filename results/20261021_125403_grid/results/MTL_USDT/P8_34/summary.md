# EMA Hourly Continuation — MTL/USDT P8_34

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 847 |
| net_profit_factor | 0.6960 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -3.8117 |
| sortino_ratio | -1.5834 |
| max_drawdown | 0.8441 |
| cagr | -0.5186 |
| net_avg_win | 46.2092 |
| net_avg_loss | -64.3892 |
| avg_hold_time_bars | 9.4038 |
| exposure | 0.3604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
