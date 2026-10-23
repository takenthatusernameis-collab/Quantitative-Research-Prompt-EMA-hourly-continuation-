# EMA Hourly Continuation — AXL/USDT P20_34

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1232 |
| net_profit_factor | 0.4460 |
| net_win_rate | 0.3872 |
| gross_profit_factor | 0.8761 |
| gross_win_rate | 0.4067 |
| sharpe_ratio | -11.3012 |
| sortino_ratio | -5.5950 |
| max_drawdown | 0.9992 |
| cagr | -0.9399 |
| net_avg_win | 16.8660 |
| net_avg_loss | -23.8897 |
| avg_hold_time_bars | 3.0333 |
| exposure | 0.1691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
