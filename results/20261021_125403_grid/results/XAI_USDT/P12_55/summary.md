# EMA Hourly Continuation — XAI/USDT P12_55

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.7495 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9266 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -2.9624 |
| sortino_ratio | -1.1077 |
| max_drawdown | 0.7465 |
| cagr | -0.3999 |
| net_avg_win | 66.7330 |
| net_avg_loss | -78.6038 |
| avg_hold_time_bars | 12.0000 |
| exposure | 0.3769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
