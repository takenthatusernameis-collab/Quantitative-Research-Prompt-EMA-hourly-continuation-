# EMA Hourly Continuation — KAS/USDT P26_89

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7496 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.8460 |
| sortino_ratio | -0.5516 |
| max_drawdown | 0.4703 |
| cagr | -0.2236 |
| net_avg_win | 65.4864 |
| net_avg_loss | -84.9889 |
| avg_hold_time_bars | 12.6560 |
| exposure | 0.2508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
