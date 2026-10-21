# EMA Hourly Continuation — CHZ/USDT P26_89

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.8201 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0509 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.2751 |
| sortino_ratio | -0.3889 |
| max_drawdown | 0.4159 |
| cagr | -0.1649 |
| net_avg_win | 71.8284 |
| net_avg_loss | -92.3845 |
| avg_hold_time_bars | 14.9044 |
| exposure | 0.3049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
