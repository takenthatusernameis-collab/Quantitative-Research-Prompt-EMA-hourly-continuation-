# EMA Hourly Continuation — ZKJ/USDT P50_89

**Symbol:** ZKJ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.1710 |
| net_win_rate | 0.3416 |
| gross_profit_factor | 0.5337 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -12.3840 |
| sortino_ratio | -5.3279 |
| max_drawdown | 0.9993 |
| cagr | -0.9448 |
| net_avg_win | 6.7799 |
| net_avg_loss | -20.5703 |
| avg_hold_time_bars | 5.4989 |
| exposure | 0.2225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
