# EMA Hourly Continuation — IO/USDT P21_100

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.6521 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9153 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -3.8479 |
| sortino_ratio | -1.4570 |
| max_drawdown | 0.8140 |
| cagr | -0.5013 |
| net_avg_win | 46.9294 |
| net_avg_loss | -64.5478 |
| avg_hold_time_bars | 11.9838 |
| exposure | 0.3951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
