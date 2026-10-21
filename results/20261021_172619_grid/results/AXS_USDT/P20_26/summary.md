# EMA Hourly Continuation — AXS/USDT P20_26

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.8655 |
| sortino_ratio | -0.3463 |
| max_drawdown | 0.3492 |
| cagr | -0.1468 |
| net_avg_win | 71.6446 |
| net_avg_loss | -104.6287 |
| avg_hold_time_bars | 4.9345 |
| exposure | 0.0375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
