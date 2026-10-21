# EMA Hourly Continuation — IMX/USDT P8_144

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.9952 |
| net_win_rate | 0.5426 |
| gross_profit_factor | 1.1704 |
| gross_win_rate | 0.5426 |
| sharpe_ratio | 0.0341 |
| sortino_ratio | 0.0097 |
| max_drawdown | 0.1577 |
| cagr | -0.0034 |
| net_avg_win | 85.5227 |
| net_avg_loss | -101.9571 |
| avg_hold_time_bars | 42.1602 |
| exposure | 0.7383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
