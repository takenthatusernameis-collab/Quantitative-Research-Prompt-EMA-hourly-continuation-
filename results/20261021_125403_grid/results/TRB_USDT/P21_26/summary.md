# EMA Hourly Continuation — TRB/USDT P21_26

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.4286 |
| net_win_rate | 0.3744 |
| gross_profit_factor | 0.6263 |
| gross_win_rate | 0.3744 |
| sharpe_ratio | -3.8332 |
| sortino_ratio | -0.7625 |
| max_drawdown | 0.5975 |
| cagr | -0.2989 |
| net_avg_win | 60.8102 |
| net_avg_loss | -84.8929 |
| avg_hold_time_bars | 4.6462 |
| exposure | 0.0410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
