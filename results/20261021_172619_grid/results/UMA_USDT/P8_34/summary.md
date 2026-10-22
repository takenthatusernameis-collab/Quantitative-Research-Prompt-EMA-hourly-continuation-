# EMA Hourly Continuation — UMA/USDT P8_34

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.6897 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -3.5280 |
| sortino_ratio | -1.4383 |
| max_drawdown | 0.8177 |
| cagr | -0.4835 |
| net_avg_win | 45.5651 |
| net_avg_loss | -62.2807 |
| avg_hold_time_bars | 8.2174 |
| exposure | 0.3040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
