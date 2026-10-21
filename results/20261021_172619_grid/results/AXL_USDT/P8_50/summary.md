# EMA Hourly Continuation — AXL/USDT P8_50

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8955 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -3.3301 |
| sortino_ratio | -1.3076 |
| max_drawdown | 0.7975 |
| cagr | -0.4534 |
| net_avg_win | 55.7430 |
| net_avg_loss | -67.1502 |
| avg_hold_time_bars | 13.1094 |
| exposure | 0.4556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
