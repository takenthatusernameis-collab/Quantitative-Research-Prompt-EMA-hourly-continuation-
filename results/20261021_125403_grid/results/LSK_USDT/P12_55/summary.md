# EMA Hourly Continuation — LSK/USDT P12_55

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.7041 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9611 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -3.2044 |
| sortino_ratio | -1.2038 |
| max_drawdown | 0.7759 |
| cagr | -0.4241 |
| net_avg_win | 53.5947 |
| net_avg_loss | -70.6024 |
| avg_hold_time_bars | 10.8237 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
