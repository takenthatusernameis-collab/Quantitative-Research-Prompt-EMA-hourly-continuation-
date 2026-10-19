# EMA Hourly Continuation — IMX/USDT P89_200

**Symbol:** IMX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6968 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0116 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -2.0959 |
| sortino_ratio | -0.5883 |
| max_drawdown | 0.5138 |
| cagr | -0.2413 |
| net_avg_win | 58.5453 |
| net_avg_loss | -84.8775 |
| avg_hold_time_bars | 11.1913 |
| exposure | 0.1985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
