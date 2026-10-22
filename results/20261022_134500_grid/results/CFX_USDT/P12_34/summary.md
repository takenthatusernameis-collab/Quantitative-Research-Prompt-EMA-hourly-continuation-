# EMA Hourly Continuation — CFX/USDT P12_34

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1273 |
| net_profit_factor | 0.4201 |
| net_win_rate | 0.4038 |
| gross_profit_factor | 0.8073 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -10.7160 |
| sortino_ratio | -5.3970 |
| max_drawdown | 0.9989 |
| cagr | -0.9337 |
| net_avg_win | 14.0763 |
| net_avg_loss | -22.6934 |
| avg_hold_time_bars | 4.1524 |
| exposure | 0.2403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
