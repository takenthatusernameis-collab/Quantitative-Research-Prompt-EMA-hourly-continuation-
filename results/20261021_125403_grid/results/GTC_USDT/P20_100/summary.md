# EMA Hourly Continuation — GTC/USDT P20_100

**Symbol:** GTC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7091 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.8887 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.4244 |
| sortino_ratio | -0.7771 |
| max_drawdown | 0.6124 |
| cagr | -0.3009 |
| net_avg_win | 60.2185 |
| net_avg_loss | -76.0520 |
| avg_hold_time_bars | 17.4331 |
| exposure | 0.4025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
