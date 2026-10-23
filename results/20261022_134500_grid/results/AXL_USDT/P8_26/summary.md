# EMA Hourly Continuation — AXL/USDT P8_26

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1594 |
| net_profit_factor | 0.5532 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -9.7330 |
| sortino_ratio | -5.4659 |
| max_drawdown | 0.9988 |
| cagr | -0.9296 |
| net_avg_win | 18.0238 |
| net_avg_loss | -24.6167 |
| avg_hold_time_bars | 4.1593 |
| exposure | 0.3000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
