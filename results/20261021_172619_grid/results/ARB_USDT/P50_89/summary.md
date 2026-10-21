# EMA Hourly Continuation — ARB/USDT P50_89

**Symbol:** ARB/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -2.0228 |
| sortino_ratio | -0.5484 |
| max_drawdown | 0.4882 |
| cagr | -0.2226 |
| net_avg_win | 64.5725 |
| net_avg_loss | -86.0672 |
| avg_hold_time_bars | 7.6992 |
| exposure | 0.1256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
