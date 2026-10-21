# EMA Hourly Continuation — XLM/USDT P34_144

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8083 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0779 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -1.1456 |
| sortino_ratio | -0.3078 |
| max_drawdown | 0.3244 |
| cagr | -0.1321 |
| net_avg_win | 69.7203 |
| net_avg_loss | -93.4913 |
| avg_hold_time_bars | 23.9109 |
| exposure | 0.3782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
