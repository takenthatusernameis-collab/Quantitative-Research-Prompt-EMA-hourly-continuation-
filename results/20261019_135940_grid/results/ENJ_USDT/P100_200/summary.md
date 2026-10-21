# EMA Hourly Continuation — ENJ/USDT P100_200

**Symbol:** ENJ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6524 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -2.3484 |
| sortino_ratio | -0.6071 |
| max_drawdown | 0.5249 |
| cagr | -0.2527 |
| net_avg_win | 57.8038 |
| net_avg_loss | -88.5973 |
| avg_hold_time_bars | 13.1657 |
| exposure | 0.2014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
