# EMA Hourly Continuation — TWT/USDT P89_100

**Symbol:** TWT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 123 |
| net_profit_factor | 0.4501 |
| net_win_rate | 0.4309 |
| gross_profit_factor | 0.7700 |
| gross_win_rate | 0.4309 |
| sharpe_ratio | -2.7118 |
| sortino_ratio | -0.4330 |
| max_drawdown | 0.4185 |
| cagr | -0.1811 |
| net_avg_win | 60.9423 |
| net_avg_loss | -102.5092 |
| avg_hold_time_bars | 4.3740 |
| exposure | 0.0245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
