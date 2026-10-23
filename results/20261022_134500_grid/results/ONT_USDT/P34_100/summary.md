# EMA Hourly Continuation — ONT/USDT P34_100

**Symbol:** ONT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5132 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -5.1074 |
| sortino_ratio | -1.8001 |
| max_drawdown | 0.8913 |
| cagr | -0.5780 |
| net_avg_win | 33.7405 |
| net_avg_loss | -51.1563 |
| avg_hold_time_bars | 10.1232 |
| exposure | 0.2900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
