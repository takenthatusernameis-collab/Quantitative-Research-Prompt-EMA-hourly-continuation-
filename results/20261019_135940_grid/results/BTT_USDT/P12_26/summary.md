# EMA Hourly Continuation — BTT/USDT P12_26

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1483 |
| net_profit_factor | 0.2046 |
| net_win_rate | 0.2994 |
| gross_profit_factor | 0.7006 |
| gross_win_rate | 0.3837 |
| sharpe_ratio | -19.6174 |
| sortino_ratio | -11.4347 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 5.7945 |
| net_avg_loss | -12.1008 |
| avg_hold_time_bars | 3.0762 |
| exposure | 0.2074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
