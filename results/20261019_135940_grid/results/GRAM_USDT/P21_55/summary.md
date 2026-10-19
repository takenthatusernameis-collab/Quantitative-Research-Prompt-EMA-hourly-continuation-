# EMA Hourly Continuation — GRAM/USDT P21_55

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.3485 |
| net_win_rate | 0.4129 |
| gross_profit_factor | 0.7783 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -9.7316 |
| sortino_ratio | -4.3720 |
| max_drawdown | 0.9961 |
| cagr | -0.8884 |
| net_avg_win | 12.8389 |
| net_avg_loss | -25.9112 |
| avg_hold_time_bars | 4.7164 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
