# EMA Hourly Continuation — SWFTC/USDT P55_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7769 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.4541 |
| sortino_ratio | -0.3583 |
| max_drawdown | 0.3684 |
| cagr | -0.1529 |
| net_avg_win | 81.8225 |
| net_avg_loss | -99.8131 |
| avg_hold_time_bars | 21.4195 |
| exposure | 0.2901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
