# EMA Hourly Continuation — HNT/USDT P34_89

**Symbol:** HNT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7771 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 0.9716 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.4318 |
| sortino_ratio | -0.4221 |
| max_drawdown | 0.4381 |
| cagr | -0.1774 |
| net_avg_win | 63.7754 |
| net_avg_loss | -82.4528 |
| avg_hold_time_bars | 12.1466 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
