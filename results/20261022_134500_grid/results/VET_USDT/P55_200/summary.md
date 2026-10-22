# EMA Hourly Continuation — VET/USDT P55_200

**Symbol:** VET/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6214 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9118 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.9144 |
| sortino_ratio | -0.8311 |
| max_drawdown | 0.6378 |
| cagr | -0.3250 |
| net_avg_win | 52.5366 |
| net_avg_loss | -78.9075 |
| avg_hold_time_bars | 19.5148 |
| exposure | 0.3601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
