# EMA Hourly Continuation — SSV/USDT P34_89

**Symbol:** SSV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7335 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -2.0205 |
| sortino_ratio | -0.6139 |
| max_drawdown | 0.5384 |
| cagr | -0.2458 |
| net_avg_win | 63.4000 |
| net_avg_loss | -81.9888 |
| avg_hold_time_bars | 12.1894 |
| exposure | 0.2504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
