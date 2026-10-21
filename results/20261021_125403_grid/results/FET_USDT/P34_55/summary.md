# EMA Hourly Continuation — FET/USDT P34_55

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7073 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9172 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -1.6355 |
| sortino_ratio | -0.3660 |
| max_drawdown | 0.3536 |
| cagr | -0.1544 |
| net_avg_win | 70.4020 |
| net_avg_loss | -92.4778 |
| avg_hold_time_bars | 5.9714 |
| exposure | 0.0665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
