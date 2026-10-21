# EMA Hourly Continuation — ENS/USDT P34_55

**Symbol:** ENS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7793 |
| net_win_rate | 0.5262 |
| gross_profit_factor | 1.1012 |
| gross_win_rate | 0.5262 |
| sharpe_ratio | -1.3609 |
| sortino_ratio | -0.3541 |
| max_drawdown | 0.3386 |
| cagr | -0.1498 |
| net_avg_win | 69.1511 |
| net_avg_loss | -98.5253 |
| avg_hold_time_bars | 5.8862 |
| exposure | 0.0870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
