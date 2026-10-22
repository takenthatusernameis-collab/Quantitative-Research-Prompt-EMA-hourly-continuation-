# EMA Hourly Continuation — MEW/USDT P26_50

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7488 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0059 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -1.8317 |
| sortino_ratio | -0.5460 |
| max_drawdown | 0.4717 |
| cagr | -0.2214 |
| net_avg_win | 63.7994 |
| net_avg_loss | -87.2042 |
| avg_hold_time_bars | 5.7262 |
| exposure | 0.1122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
