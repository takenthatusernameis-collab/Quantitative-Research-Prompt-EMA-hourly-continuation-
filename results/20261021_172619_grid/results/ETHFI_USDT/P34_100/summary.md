# EMA Hourly Continuation — ETHFI/USDT P34_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.8776 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0561 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -0.9398 |
| sortino_ratio | -0.2776 |
| max_drawdown | 0.4094 |
| cagr | -0.1226 |
| net_avg_win | 92.9270 |
| net_avg_loss | -110.4889 |
| avg_hold_time_bars | 14.3404 |
| exposure | 0.2757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
