# EMA Hourly Continuation — KNC/USDT P21_144

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 1.0046 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.6615 |
| sortino_ratio | -0.7873 |
| max_drawdown | 0.6535 |
| cagr | -0.3173 |
| net_avg_win | 61.1453 |
| net_avg_loss | -86.4212 |
| avg_hold_time_bars | 28.3893 |
| exposure | 0.5768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
