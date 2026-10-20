# EMA Hourly Continuation — DEEP/USDT P26_89

**Symbol:** DEEP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7360 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -2.5031 |
| sortino_ratio | -0.9003 |
| max_drawdown | 0.5785 |
| cagr | -0.3431 |
| net_avg_win | 62.4638 |
| net_avg_loss | -83.8842 |
| avg_hold_time_bars | 9.9649 |
| exposure | 0.2894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
