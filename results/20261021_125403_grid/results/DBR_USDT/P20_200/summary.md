# EMA Hourly Continuation — DBR/USDT P20_200

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.6185 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.7799 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -2.4491 |
| sortino_ratio | -0.5991 |
| max_drawdown | 0.4428 |
| cagr | -0.2420 |
| net_avg_win | 64.6389 |
| net_avg_loss | -84.7149 |
| avg_hold_time_bars | 45.0669 |
| exposure | 0.6125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
