# EMA Hourly Continuation — ATH/USDT P34_144

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7518 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.0935 |
| gross_win_rate | 0.5247 |
| sharpe_ratio | -2.0268 |
| sortino_ratio | -0.6532 |
| max_drawdown | 0.5313 |
| cagr | -0.2665 |
| net_avg_win | 62.2577 |
| net_avg_loss | -89.1823 |
| avg_hold_time_bars | 16.8004 |
| exposure | 0.3958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
