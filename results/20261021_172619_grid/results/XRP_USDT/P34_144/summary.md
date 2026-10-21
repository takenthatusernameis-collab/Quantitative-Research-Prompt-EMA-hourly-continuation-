# EMA Hourly Continuation — XRP/USDT P34_144

**Symbol:** XRP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9605 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.9397 |
| sortino_ratio | -0.5037 |
| max_drawdown | 0.4769 |
| cagr | -0.2061 |
| net_avg_win | 63.5127 |
| net_avg_loss | -87.9477 |
| avg_hold_time_bars | 25.9210 |
| exposure | 0.3876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
