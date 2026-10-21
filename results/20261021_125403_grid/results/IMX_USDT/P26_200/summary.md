# EMA Hourly Continuation — IMX/USDT P26_200

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 1.1185 |
| net_win_rate | 0.5654 |
| gross_profit_factor | 1.3128 |
| gross_win_rate | 0.5654 |
| sharpe_ratio | 0.6116 |
| sortino_ratio | 0.1559 |
| max_drawdown | 0.1134 |
| cagr | 0.0629 |
| net_avg_win | 90.7725 |
| net_avg_loss | -105.5627 |
| avg_hold_time_bars | 43.2778 |
| exposure | 0.5993 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
