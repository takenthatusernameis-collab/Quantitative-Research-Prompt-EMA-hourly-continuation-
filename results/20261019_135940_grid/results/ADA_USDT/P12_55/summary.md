# EMA Hourly Continuation — ADA/USDT P12_55

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.4873 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8707 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -6.9580 |
| sortino_ratio | -3.0873 |
| max_drawdown | 0.9785 |
| cagr | -0.7812 |
| net_avg_win | 20.5206 |
| net_avg_loss | -34.5573 |
| avg_hold_time_bars | 8.0607 |
| exposure | 0.3682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
