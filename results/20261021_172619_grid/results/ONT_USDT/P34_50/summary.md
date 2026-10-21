# EMA Hourly Continuation — ONT/USDT P34_50

**Symbol:** ONT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6543 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9813 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.4856 |
| sortino_ratio | -0.6148 |
| max_drawdown | 0.5360 |
| cagr | -0.2466 |
| net_avg_win | 66.6408 |
| net_avg_loss | -96.5217 |
| avg_hold_time_bars | 4.9631 |
| exposure | 0.0669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
