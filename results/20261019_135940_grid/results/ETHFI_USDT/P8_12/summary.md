# EMA Hourly Continuation — ETHFI/USDT P8_12

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1848 |
| net_profit_factor | 0.2424 |
| net_win_rate | 0.3674 |
| gross_profit_factor | 0.6046 |
| gross_win_rate | 0.3999 |
| sharpe_ratio | -16.7769 |
| sortino_ratio | -10.3342 |
| max_drawdown | 1.0000 |
| cagr | -0.9956 |
| net_avg_win | 4.7112 |
| net_avg_loss | -11.2908 |
| avg_hold_time_bars | 1.6580 |
| exposure | 0.1393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
