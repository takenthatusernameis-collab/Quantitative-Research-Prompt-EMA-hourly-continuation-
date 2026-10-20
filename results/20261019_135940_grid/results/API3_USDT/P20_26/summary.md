# EMA Hourly Continuation — API3/USDT P20_26

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1245 |
| net_profit_factor | 0.3087 |
| net_win_rate | 0.3807 |
| gross_profit_factor | 0.8196 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -13.3212 |
| sortino_ratio | -6.7597 |
| max_drawdown | 0.9999 |
| cagr | -0.9704 |
| net_avg_win | 9.4183 |
| net_avg_loss | -18.7585 |
| avg_hold_time_bars | 2.2795 |
| exposure | 0.1290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
