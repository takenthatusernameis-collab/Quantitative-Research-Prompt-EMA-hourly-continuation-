# EMA Hourly Continuation — ICP/USDT P21_55

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7069 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9298 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.4613 |
| sortino_ratio | -0.7760 |
| max_drawdown | 0.6076 |
| cagr | -0.2994 |
| net_avg_win | 60.8983 |
| net_avg_loss | -79.6797 |
| avg_hold_time_bars | 8.7310 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
