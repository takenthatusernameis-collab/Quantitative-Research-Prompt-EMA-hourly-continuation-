# EMA Hourly Continuation — CRO/USDT P20_26

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.5308 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -2.8654 |
| sortino_ratio | -0.5943 |
| max_drawdown | 0.5173 |
| cagr | -0.2401 |
| net_avg_win | 58.7197 |
| net_avg_loss | -94.8156 |
| avg_hold_time_bars | 4.9471 |
| exposure | 0.0468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
