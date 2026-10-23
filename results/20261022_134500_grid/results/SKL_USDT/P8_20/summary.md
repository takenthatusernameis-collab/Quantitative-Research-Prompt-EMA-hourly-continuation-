# EMA Hourly Continuation — SKL/USDT P8_20

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1791 |
| net_profit_factor | 0.4155 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -11.4259 |
| sortino_ratio | -6.8139 |
| max_drawdown | 0.9998 |
| cagr | -0.9661 |
| net_avg_win | 8.9726 |
| net_avg_loss | -17.1214 |
| avg_hold_time_bars | 2.6778 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
