# EMA Hourly Continuation — WLD/USDT P50_200

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7385 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9299 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -1.6061 |
| sortino_ratio | -0.3957 |
| max_drawdown | 0.4217 |
| cagr | -0.1710 |
| net_avg_win | 71.6634 |
| net_avg_loss | -91.4797 |
| avg_hold_time_bars | 29.6295 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
