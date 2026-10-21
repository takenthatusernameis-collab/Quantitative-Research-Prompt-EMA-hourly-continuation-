# EMA Hourly Continuation — SKL/USDT P34_89

**Symbol:** SKL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7050 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -2.2730 |
| sortino_ratio | -0.6743 |
| max_drawdown | 0.5687 |
| cagr | -0.2661 |
| net_avg_win | 62.9868 |
| net_avg_loss | -80.3252 |
| avg_hold_time_bars | 12.6628 |
| exposure | 0.2492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
