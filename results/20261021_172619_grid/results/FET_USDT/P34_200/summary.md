# EMA Hourly Continuation — FET/USDT P34_200

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.9240 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0638 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.3440 |
| sortino_ratio | -0.0817 |
| max_drawdown | 0.1440 |
| cagr | -0.0405 |
| net_avg_win | 84.3590 |
| net_avg_loss | -98.9616 |
| avg_hold_time_bars | 38.4103 |
| exposure | 0.4766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
