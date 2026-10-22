# EMA Hourly Continuation — TNSR/USDT P55_89

**Symbol:** TNSR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7655 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.7103 |
| sortino_ratio | -0.4670 |
| max_drawdown | 0.4678 |
| cagr | -0.1933 |
| net_avg_win | 74.6356 |
| net_avg_loss | -98.5746 |
| avg_hold_time_bars | 6.6566 |
| exposure | 0.1097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
