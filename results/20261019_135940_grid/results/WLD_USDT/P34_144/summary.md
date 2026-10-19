# EMA Hourly Continuation — WLD/USDT P34_144

**Symbol:** WLD/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7568 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.7161 |
| sortino_ratio | -0.5018 |
| max_drawdown | 0.5053 |
| cagr | -0.2129 |
| net_avg_win | 64.5120 |
| net_avg_loss | -87.6542 |
| avg_hold_time_bars | 20.5953 |
| exposure | 0.4025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
