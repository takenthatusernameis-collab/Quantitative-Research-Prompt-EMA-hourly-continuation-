# EMA Hourly Continuation — SUI/USDT P26_144

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7196 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0782 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -2.4720 |
| sortino_ratio | -0.7839 |
| max_drawdown | 0.6457 |
| cagr | -0.3153 |
| net_avg_win | 61.2740 |
| net_avg_loss | -87.1908 |
| avg_hold_time_bars | 19.4409 |
| exposure | 0.4489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
