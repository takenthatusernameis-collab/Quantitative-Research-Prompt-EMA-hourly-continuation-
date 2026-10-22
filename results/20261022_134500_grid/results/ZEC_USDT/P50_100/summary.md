# EMA Hourly Continuation — ZEC/USDT P50_100

**Symbol:** ZEC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.5743 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 1.0125 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -4.3398 |
| sortino_ratio | -1.5224 |
| max_drawdown | 0.8496 |
| cagr | -0.5180 |
| net_avg_win | 38.4152 |
| net_avg_loss | -60.5297 |
| avg_hold_time_bars | 5.1739 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
