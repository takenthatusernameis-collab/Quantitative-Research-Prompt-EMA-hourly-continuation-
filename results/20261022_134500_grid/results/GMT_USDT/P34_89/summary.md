# EMA Hourly Continuation — GMT/USDT P34_89

**Symbol:** GMT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.9260 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -5.8687 |
| sortino_ratio | -2.2292 |
| max_drawdown | 0.9351 |
| cagr | -0.6564 |
| net_avg_win | 36.2293 |
| net_avg_loss | -51.4504 |
| avg_hold_time_bars | 6.8326 |
| exposure | 0.2245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
