# EMA Hourly Continuation — MOODENG/USDT P20_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6345 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8723 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -4.2990 |
| sortino_ratio | -1.6484 |
| max_drawdown | 0.8167 |
| cagr | -0.5462 |
| net_avg_win | 50.0336 |
| net_avg_loss | -65.8673 |
| avg_hold_time_bars | 11.3507 |
| exposure | 0.3850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
