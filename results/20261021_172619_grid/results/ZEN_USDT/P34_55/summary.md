# EMA Hourly Continuation — ZEN/USDT P34_55

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6577 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9153 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.4091 |
| sortino_ratio | -0.6643 |
| max_drawdown | 0.5575 |
| cagr | -0.2634 |
| net_avg_win | 57.5421 |
| net_avg_loss | -81.5602 |
| avg_hold_time_bars | 5.2507 |
| exposure | 0.0885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
