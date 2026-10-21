# EMA Hourly Continuation — CFX/USDT P8_55

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.7858 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.0253 |
| sortino_ratio | -0.7269 |
| max_drawdown | 0.5857 |
| cagr | -0.2848 |
| net_avg_win | 67.3197 |
| net_avg_loss | -82.9976 |
| avg_hold_time_bars | 16.7698 |
| exposure | 0.4802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
