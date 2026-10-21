# EMA Hourly Continuation — ADA/USDT P26_34

**Symbol:** ADA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.7084 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0028 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.4556 |
| sortino_ratio | -0.2703 |
| max_drawdown | 0.3194 |
| cagr | -0.1161 |
| net_avg_win | 78.0383 |
| net_avg_loss | -108.8431 |
| avg_hold_time_bars | 5.1497 |
| exposure | 0.0391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
