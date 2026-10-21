# EMA Hourly Continuation — AKT/USDT P21_100

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8122 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9698 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.3945 |
| sortino_ratio | -0.4212 |
| max_drawdown | 0.3996 |
| cagr | -0.1780 |
| net_avg_win | 76.3990 |
| net_avg_loss | -91.1647 |
| avg_hold_time_bars | 18.6331 |
| exposure | 0.3786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
