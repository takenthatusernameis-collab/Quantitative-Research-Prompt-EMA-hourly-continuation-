# EMA Hourly Continuation — CAKE/USDT P55_200

**Symbol:** CAKE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9533 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9258 |
| sortino_ratio | -0.7846 |
| max_drawdown | 0.6560 |
| cagr | -0.3169 |
| net_avg_win | 49.3878 |
| net_avg_loss | -80.2146 |
| avg_hold_time_bars | 19.7596 |
| exposure | 0.3287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
