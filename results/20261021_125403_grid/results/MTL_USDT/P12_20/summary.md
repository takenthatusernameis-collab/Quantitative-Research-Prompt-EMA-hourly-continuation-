# EMA Hourly Continuation — MTL/USDT P12_20

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.5143 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -5.5214 |
| sortino_ratio | -1.8919 |
| max_drawdown | 0.8978 |
| cagr | -0.5906 |
| net_avg_win | 36.0262 |
| net_avg_loss | -59.4325 |
| avg_hold_time_bars | 4.9860 |
| exposure | 0.1293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
