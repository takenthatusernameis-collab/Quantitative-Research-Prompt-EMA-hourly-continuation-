# EMA Hourly Continuation — XMR/USDT P50_144

**Symbol:** XMR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.3799 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.7585 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -7.7131 |
| sortino_ratio | -3.0835 |
| max_drawdown | 0.9781 |
| cagr | -0.7808 |
| net_avg_win | 17.7739 |
| net_avg_loss | -34.2797 |
| avg_hold_time_bars | 7.0828 |
| exposure | 0.2566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
