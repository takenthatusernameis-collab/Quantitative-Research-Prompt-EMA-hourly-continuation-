# EMA Hourly Continuation — IMX/USDT P8_200

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 1.2102 |
| net_win_rate | 0.5799 |
| gross_profit_factor | 1.3942 |
| gross_win_rate | 0.5799 |
| sharpe_ratio | 0.9746 |
| sortino_ratio | 0.2344 |
| max_drawdown | 0.0992 |
| cagr | 0.0995 |
| net_avg_win | 99.7413 |
| net_avg_loss | -113.7831 |
| avg_hold_time_bars | 67.2156 |
| exposure | 0.8182 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
