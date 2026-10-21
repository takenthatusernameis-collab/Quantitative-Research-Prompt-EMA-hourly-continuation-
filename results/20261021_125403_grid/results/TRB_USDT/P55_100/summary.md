# EMA Hourly Continuation — TRB/USDT P55_100

**Symbol:** TRB/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6858 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.2071 |
| sortino_ratio | -0.5831 |
| max_drawdown | 0.5122 |
| cagr | -0.2333 |
| net_avg_win | 64.6031 |
| net_avg_loss | -87.3238 |
| avg_hold_time_bars | 9.0962 |
| exposure | 0.1412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
