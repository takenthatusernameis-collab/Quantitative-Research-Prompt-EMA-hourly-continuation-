# EMA Hourly Continuation — ATH/USDT P20_26

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 159 |
| net_profit_factor | 0.9800 |
| net_win_rate | 0.5723 |
| gross_profit_factor | 1.3265 |
| gross_win_rate | 0.5723 |
| sharpe_ratio | -0.0458 |
| sortino_ratio | -0.0087 |
| max_drawdown | 0.1544 |
| cagr | -0.0071 |
| net_avg_win | 89.6156 |
| net_avg_loss | -122.3715 |
| avg_hold_time_bars | 4.5346 |
| exposure | 0.0349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
