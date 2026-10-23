# EMA Hourly Continuation — MTL/USDT P20_34

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1081 |
| net_profit_factor | 0.3174 |
| net_win_rate | 0.3913 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -11.5686 |
| sortino_ratio | -5.4270 |
| max_drawdown | 0.9991 |
| cagr | -0.9386 |
| net_avg_win | 10.9832 |
| net_avg_loss | -22.2448 |
| avg_hold_time_bars | 3.7280 |
| exposure | 0.1824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
