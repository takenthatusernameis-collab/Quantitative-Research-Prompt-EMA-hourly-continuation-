# EMA Hourly Continuation — XAI/USDT P50_89

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7234 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.2058 |
| sortino_ratio | -0.6259 |
| max_drawdown | 0.5736 |
| cagr | -0.2502 |
| net_avg_win | 70.8552 |
| net_avg_loss | -91.2234 |
| avg_hold_time_bars | 8.2360 |
| exposure | 0.1475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
