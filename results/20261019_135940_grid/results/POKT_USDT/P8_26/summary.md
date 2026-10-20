# EMA Hourly Continuation — POKT/USDT P8_26

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1557 |
| net_profit_factor | 0.4129 |
| net_win_rate | 0.3674 |
| gross_profit_factor | 0.8133 |
| gross_win_rate | 0.3873 |
| sharpe_ratio | -12.5756 |
| sortino_ratio | -6.9554 |
| max_drawdown | 0.9998 |
| cagr | -0.9686 |
| net_avg_win | 12.2935 |
| net_avg_loss | -17.2896 |
| avg_hold_time_bars | 4.1092 |
| exposure | 0.2895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
