# EMA Hourly Continuation — MEW/USDT P34_200

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9535 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -1.6976 |
| sortino_ratio | -0.4334 |
| max_drawdown | 0.4594 |
| cagr | -0.1833 |
| net_avg_win | 72.2514 |
| net_avg_loss | -92.7846 |
| avg_hold_time_bars | 35.6883 |
| exposure | 0.5256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
