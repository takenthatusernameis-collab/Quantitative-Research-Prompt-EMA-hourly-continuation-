# EMA Hourly Continuation — MOG/USDT P20_21

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1089 |
| net_profit_factor | 0.3391 |
| net_win_rate | 0.3572 |
| gross_profit_factor | 0.7055 |
| gross_win_rate | 0.3976 |
| sharpe_ratio | -14.1147 |
| sortino_ratio | -6.9807 |
| max_drawdown | 0.9999 |
| cagr | -0.9789 |
| net_avg_win | 13.1854 |
| net_avg_loss | -21.6110 |
| avg_hold_time_bars | 1.9164 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
