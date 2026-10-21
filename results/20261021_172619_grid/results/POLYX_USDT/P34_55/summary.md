# EMA Hourly Continuation — POLYX/USDT P34_55

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0097 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -2.6956 |
| sortino_ratio | -0.8206 |
| max_drawdown | 0.6402 |
| cagr | -0.3130 |
| net_avg_win | 57.6654 |
| net_avg_loss | -85.1783 |
| avg_hold_time_bars | 5.4566 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
