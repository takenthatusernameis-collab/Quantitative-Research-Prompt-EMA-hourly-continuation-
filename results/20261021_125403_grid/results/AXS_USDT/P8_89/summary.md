# EMA Hourly Continuation — AXS/USDT P8_89

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.9006 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.1077 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.7101 |
| sortino_ratio | -0.2282 |
| max_drawdown | 0.3038 |
| cagr | -0.1040 |
| net_avg_win | 83.0304 |
| net_avg_loss | -103.1369 |
| avg_hold_time_bars | 27.9020 |
| exposure | 0.6313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
