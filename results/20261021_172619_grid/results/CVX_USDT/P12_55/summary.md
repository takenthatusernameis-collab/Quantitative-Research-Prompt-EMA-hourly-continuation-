# EMA Hourly Continuation — CVX/USDT P12_55

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.8480 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0598 |
| gross_win_rate | 0.5182 |
| sharpe_ratio | -1.2609 |
| sortino_ratio | -0.4655 |
| max_drawdown | 0.4346 |
| cagr | -0.1960 |
| net_avg_win | 68.8342 |
| net_avg_loss | -87.2959 |
| avg_hold_time_bars | 11.4864 |
| exposure | 0.3446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
