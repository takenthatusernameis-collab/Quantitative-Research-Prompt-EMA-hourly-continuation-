# EMA Hourly Continuation — QNT/USDT P50_89

**Symbol:** QNT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9379 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.4674 |
| sortino_ratio | -0.6881 |
| max_drawdown | 0.5766 |
| cagr | -0.2691 |
| net_avg_win | 54.0684 |
| net_avg_loss | -80.4746 |
| avg_hold_time_bars | 6.4032 |
| exposure | 0.1097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
