# EMA Hourly Continuation — VR/USDT P144_200

**Symbol:** VR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.5047 |
| net_win_rate | 0.3771 |
| gross_profit_factor | 0.6470 |
| gross_win_rate | 0.3771 |
| sharpe_ratio | -3.1188 |
| sortino_ratio | -0.5822 |
| max_drawdown | 0.5056 |
| cagr | -0.2393 |
| net_avg_win | 76.7339 |
| net_avg_loss | -92.0529 |
| avg_hold_time_bars | 10.0286 |
| exposure | 0.0798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
