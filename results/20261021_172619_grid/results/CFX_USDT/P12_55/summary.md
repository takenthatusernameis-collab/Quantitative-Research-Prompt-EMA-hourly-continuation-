# EMA Hourly Continuation — CFX/USDT P12_55

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.7268 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9185 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -2.4818 |
| sortino_ratio | -0.8619 |
| max_drawdown | 0.6603 |
| cagr | -0.3267 |
| net_avg_win | 58.9823 |
| net_avg_loss | -74.8290 |
| avg_hold_time_bars | 13.0676 |
| exposure | 0.3516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
