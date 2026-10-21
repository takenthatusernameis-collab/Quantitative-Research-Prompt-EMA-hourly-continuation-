# EMA Hourly Continuation — T/USDT P34_144

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7337 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9893 |
| gross_win_rate | 0.4975 |
| sharpe_ratio | -1.9802 |
| sortino_ratio | -0.5596 |
| max_drawdown | 0.5046 |
| cagr | -0.2277 |
| net_avg_win | 67.6634 |
| net_avg_loss | -90.3658 |
| avg_hold_time_bars | 21.0584 |
| exposure | 0.3755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
