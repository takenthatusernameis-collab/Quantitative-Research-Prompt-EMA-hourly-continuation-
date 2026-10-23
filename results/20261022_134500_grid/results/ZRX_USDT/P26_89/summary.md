# EMA Hourly Continuation — ZRX/USDT P26_89

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6059 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9442 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -4.6479 |
| sortino_ratio | -1.6719 |
| max_drawdown | 0.8781 |
| cagr | -0.5540 |
| net_avg_win | 43.7648 |
| net_avg_loss | -62.5910 |
| avg_hold_time_bars | 11.2998 |
| exposure | 0.3375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
