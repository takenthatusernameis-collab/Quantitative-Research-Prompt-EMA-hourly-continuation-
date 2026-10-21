# EMA Hourly Continuation — CRV/USDT P8_55

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.8227 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0177 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.6083 |
| sortino_ratio | -0.5887 |
| max_drawdown | 0.5161 |
| cagr | -0.2391 |
| net_avg_win | 70.0276 |
| net_avg_loss | -86.7009 |
| avg_hold_time_bars | 15.5552 |
| exposure | 0.4610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
