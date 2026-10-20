# EMA Hourly Continuation — IO/USDT P20_200

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5901 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8013 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -3.3690 |
| sortino_ratio | -0.9386 |
| max_drawdown | 0.6706 |
| cagr | -0.3662 |
| net_avg_win | 57.1269 |
| net_avg_loss | -76.5260 |
| avg_hold_time_bars | 36.7633 |
| exposure | 0.6692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
