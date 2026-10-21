# EMA Hourly Continuation — JST/USDT P12_34

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.1077 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -4.0192 |
| sortino_ratio | -1.4398 |
| max_drawdown | 0.8158 |
| cagr | -0.4828 |
| net_avg_win | 34.0750 |
| net_avg_loss | -62.7174 |
| avg_hold_time_bars | 8.1694 |
| exposure | 0.2292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
