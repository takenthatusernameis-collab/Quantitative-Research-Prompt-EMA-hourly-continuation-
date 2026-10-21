# EMA Hourly Continuation — IO/USDT P26_89

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8055 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9631 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -1.4709 |
| sortino_ratio | -0.4629 |
| max_drawdown | 0.4333 |
| cagr | -0.1932 |
| net_avg_win | 73.4438 |
| net_avg_loss | -88.4159 |
| avg_hold_time_bars | 11.6308 |
| exposure | 0.2562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
