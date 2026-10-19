# EMA Hourly Continuation — RAY/USDT P89_200

**Symbol:** RAY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6508 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.5931 |
| sortino_ratio | -0.7412 |
| max_drawdown | 0.6216 |
| cagr | -0.2954 |
| net_avg_win | 53.9618 |
| net_avg_loss | -81.3047 |
| avg_hold_time_bars | 10.4142 |
| exposure | 0.1931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
