# EMA Hourly Continuation — ATH/USDT P12_34

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1214 |
| net_profit_factor | 0.5294 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.9208 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -7.8892 |
| sortino_ratio | -3.9739 |
| max_drawdown | 0.9911 |
| cagr | -0.8616 |
| net_avg_win | 19.9713 |
| net_avg_loss | -32.0870 |
| avg_hold_time_bars | 3.7677 |
| exposure | 0.2217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
