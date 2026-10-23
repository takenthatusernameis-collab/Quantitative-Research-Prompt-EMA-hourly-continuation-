# EMA Hourly Continuation — YGG/USDT P12_89

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.6620 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -3.8388 |
| sortino_ratio | -1.4493 |
| max_drawdown | 0.8307 |
| cagr | -0.4950 |
| net_avg_win | 47.7396 |
| net_avg_loss | -63.7901 |
| avg_hold_time_bars | 16.4708 |
| exposure | 0.5351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
