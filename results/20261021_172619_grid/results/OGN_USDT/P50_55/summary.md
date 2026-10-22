# EMA Hourly Continuation — OGN/USDT P50_55

**Symbol:** OGN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.4696 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7774 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -3.1258 |
| sortino_ratio | -0.6048 |
| max_drawdown | 0.5260 |
| cagr | -0.2461 |
| net_avg_win | 56.4055 |
| net_avg_loss | -92.3977 |
| avg_hold_time_bars | 5.4837 |
| exposure | 0.0457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
