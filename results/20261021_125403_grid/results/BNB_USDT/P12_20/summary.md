# EMA Hourly Continuation — BNB/USDT P12_20

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.5824 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.1119 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -2.4950 |
| sortino_ratio | -0.5436 |
| max_drawdown | 0.4742 |
| cagr | -0.2187 |
| net_avg_win | 56.5146 |
| net_avg_loss | -99.6575 |
| avg_hold_time_bars | 5.4800 |
| exposure | 0.0560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
