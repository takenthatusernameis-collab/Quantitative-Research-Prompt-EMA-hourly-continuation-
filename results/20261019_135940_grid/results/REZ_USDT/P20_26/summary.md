# EMA Hourly Continuation — REZ/USDT P20_26

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.3730 |
| net_win_rate | 0.3873 |
| gross_profit_factor | 0.8474 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -11.6360 |
| sortino_ratio | -5.5490 |
| max_drawdown | 0.9991 |
| cagr | -0.9415 |
| net_avg_win | 13.8869 |
| net_avg_loss | -23.5372 |
| avg_hold_time_bars | 2.6018 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
