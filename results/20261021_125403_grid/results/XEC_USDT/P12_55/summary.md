# EMA Hourly Continuation — XEC/USDT P12_55

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.7012 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.2631 |
| sortino_ratio | -1.2498 |
| max_drawdown | 0.7807 |
| cagr | -0.4361 |
| net_avg_win | 51.3956 |
| net_avg_loss | -68.9485 |
| avg_hold_time_bars | 11.9111 |
| exposure | 0.3881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
