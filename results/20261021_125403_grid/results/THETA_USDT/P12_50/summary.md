# EMA Hourly Continuation — THETA/USDT P12_50

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.7427 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9391 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.2387 |
| sortino_ratio | -0.7673 |
| max_drawdown | 0.6175 |
| cagr | -0.2966 |
| net_avg_win | 60.6879 |
| net_avg_loss | -77.0244 |
| avg_hold_time_bars | 12.4661 |
| exposure | 0.3258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
