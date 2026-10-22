# EMA Hourly Continuation — IMX/USDT P12_50

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.6320 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -4.3532 |
| sortino_ratio | -1.9512 |
| max_drawdown | 0.9096 |
| cagr | -0.6029 |
| net_avg_win | 31.2574 |
| net_avg_loss | -47.8174 |
| avg_hold_time_bars | 7.6918 |
| exposure | 0.3512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
