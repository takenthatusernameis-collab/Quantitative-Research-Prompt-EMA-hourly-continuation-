# EMA Hourly Continuation — CFX/USDT P89_200

**Symbol:** CFX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5816 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8628 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -3.0574 |
| sortino_ratio | -0.8154 |
| max_drawdown | 0.6227 |
| cagr | -0.3193 |
| net_avg_win | 52.8260 |
| net_avg_loss | -77.1048 |
| avg_hold_time_bars | 14.2563 |
| exposure | 0.2300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
