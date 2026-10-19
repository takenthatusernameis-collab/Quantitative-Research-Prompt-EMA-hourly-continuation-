# EMA Hourly Continuation — CFX/USDT P26_34

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.2535 |
| net_win_rate | 0.3792 |
| gross_profit_factor | 0.6856 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -13.0794 |
| sortino_ratio | -6.3014 |
| max_drawdown | 0.9998 |
| cagr | -0.9642 |
| net_avg_win | 8.0460 |
| net_avg_loss | -19.3822 |
| avg_hold_time_bars | 2.1123 |
| exposure | 0.1069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
