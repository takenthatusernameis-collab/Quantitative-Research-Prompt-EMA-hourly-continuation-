# EMA Hourly Continuation — TRB/USDT P21_55

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.3800 |
| net_win_rate | 0.3970 |
| gross_profit_factor | 0.6670 |
| gross_win_rate | 0.4173 |
| sharpe_ratio | -9.4412 |
| sortino_ratio | -4.1770 |
| max_drawdown | 0.9947 |
| cagr | -0.8748 |
| net_avg_win | 15.5895 |
| net_avg_loss | -27.0078 |
| avg_hold_time_bars | 5.7056 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
