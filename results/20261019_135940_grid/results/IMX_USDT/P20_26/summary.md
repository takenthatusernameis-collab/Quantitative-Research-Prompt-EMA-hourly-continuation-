# EMA Hourly Continuation — IMX/USDT P20_26

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1192 |
| net_profit_factor | 0.2554 |
| net_win_rate | 0.3884 |
| gross_profit_factor | 0.6724 |
| gross_win_rate | 0.4287 |
| sharpe_ratio | -12.6967 |
| sortino_ratio | -6.2735 |
| max_drawdown | 0.9997 |
| cagr | -0.9625 |
| net_avg_win | 7.4080 |
| net_avg_loss | -18.4189 |
| avg_hold_time_bars | 2.0436 |
| exposure | 0.1102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
