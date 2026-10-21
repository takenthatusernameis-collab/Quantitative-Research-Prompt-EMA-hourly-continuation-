# EMA Hourly Continuation — CFX/USDT P12_26

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7315 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0176 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.0406 |
| sortino_ratio | -0.5891 |
| max_drawdown | 0.5236 |
| cagr | -0.2359 |
| net_avg_win | 65.9239 |
| net_avg_loss | -91.4692 |
| avg_hold_time_bars | 6.0298 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
