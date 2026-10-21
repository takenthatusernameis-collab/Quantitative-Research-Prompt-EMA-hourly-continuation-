# EMA Hourly Continuation — WLD/USDT P34_200

**Symbol:** WLD/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.9176 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0312 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -0.3766 |
| sortino_ratio | -0.0846 |
| max_drawdown | 0.1768 |
| cagr | -0.0413 |
| net_avg_win | 89.4363 |
| net_avg_loss | -101.5341 |
| avg_hold_time_bars | 46.6327 |
| exposure | 0.5193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
