# EMA Hourly Continuation — WOO/USDT P8_55

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.7646 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -2.8165 |
| sortino_ratio | -1.0878 |
| max_drawdown | 0.7422 |
| cagr | -0.3945 |
| net_avg_win | 66.4872 |
| net_avg_loss | -78.8450 |
| avg_hold_time_bars | 13.8777 |
| exposure | 0.4643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
