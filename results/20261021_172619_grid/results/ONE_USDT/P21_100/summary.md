# EMA Hourly Continuation — ONE/USDT P21_100

**Symbol:** ONE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.8487 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0249 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.1469 |
| sortino_ratio | -0.3555 |
| max_drawdown | 0.4065 |
| cagr | -0.1531 |
| net_avg_win | 80.7275 |
| net_avg_loss | -97.5936 |
| avg_hold_time_bars | 19.7308 |
| exposure | 0.4197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
