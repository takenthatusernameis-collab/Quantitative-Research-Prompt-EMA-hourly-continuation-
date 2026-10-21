# EMA Hourly Continuation — BAT/USDT P50_144

**Symbol:** BAT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6705 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8869 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.5031 |
| sortino_ratio | -0.6975 |
| max_drawdown | 0.5628 |
| cagr | -0.2742 |
| net_avg_win | 62.8529 |
| net_avg_loss | -82.2530 |
| avg_hold_time_bars | 13.4360 |
| exposure | 0.2339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
