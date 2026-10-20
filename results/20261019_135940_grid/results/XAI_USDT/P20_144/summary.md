# EMA Hourly Continuation — XAI/USDT P20_144

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.9373 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.2800 |
| sortino_ratio | -1.0109 |
| max_drawdown | 0.7599 |
| cagr | -0.3848 |
| net_avg_win | 67.7156 |
| net_avg_loss | -85.3799 |
| avg_hold_time_bars | 27.8230 |
| exposure | 0.6146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
