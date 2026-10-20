# EMA Hourly Continuation — YGG/USDT P12_55

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.6202 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -5.2200 |
| sortino_ratio | -2.3170 |
| max_drawdown | 0.9370 |
| cagr | -0.6648 |
| net_avg_win | 32.9608 |
| net_avg_loss | -46.7033 |
| avg_hold_time_bars | 8.5514 |
| exposure | 0.3839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
