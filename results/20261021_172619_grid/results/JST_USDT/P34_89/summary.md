# EMA Hourly Continuation — JST/USDT P34_89

**Symbol:** JST/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.5390 |
| gross_profit_factor | 1.1730 |
| gross_win_rate | 0.5414 |
| sharpe_ratio | -2.5090 |
| sortino_ratio | -0.7394 |
| max_drawdown | 0.5912 |
| cagr | -0.2896 |
| net_avg_win | 47.5629 |
| net_avg_loss | -85.2506 |
| avg_hold_time_bars | 11.2648 |
| exposure | 0.2156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
