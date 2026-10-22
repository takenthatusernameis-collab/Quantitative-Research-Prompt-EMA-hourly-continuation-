# EMA Hourly Continuation — ZKJ/USDT P100_144

**Symbol:** ZKJ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.1778 |
| net_win_rate | 0.3349 |
| gross_profit_factor | 0.5870 |
| gross_win_rate | 0.4042 |
| sharpe_ratio | -10.1349 |
| sortino_ratio | -3.6266 |
| max_drawdown | 0.9925 |
| cagr | -0.8557 |
| net_avg_win | 10.3197 |
| net_avg_loss | -29.2230 |
| avg_hold_time_bars | 5.6779 |
| exposure | 0.1603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
