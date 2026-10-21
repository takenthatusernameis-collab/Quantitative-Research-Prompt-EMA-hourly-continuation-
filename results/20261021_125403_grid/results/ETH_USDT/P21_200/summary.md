# EMA Hourly Continuation — ETH/USDT P21_200

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -1.4433 |
| sortino_ratio | -0.2931 |
| max_drawdown | 0.3200 |
| cagr | -0.1264 |
| net_avg_win | 71.1933 |
| net_avg_loss | -98.0167 |
| avg_hold_time_bars | 76.9851 |
| exposure | 0.7069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
