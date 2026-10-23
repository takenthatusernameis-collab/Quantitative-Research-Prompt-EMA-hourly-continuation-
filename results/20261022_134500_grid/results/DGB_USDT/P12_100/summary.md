# EMA Hourly Continuation — DGB/USDT P12_100

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.9744 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -5.2260 |
| sortino_ratio | -2.0391 |
| max_drawdown | 0.9232 |
| cagr | -0.6347 |
| net_avg_win | 42.2027 |
| net_avg_loss | -57.0681 |
| avg_hold_time_bars | 15.6747 |
| exposure | 0.5586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
