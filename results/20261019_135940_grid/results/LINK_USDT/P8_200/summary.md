# EMA Hourly Continuation — LINK/USDT P8_200

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -2.3938 |
| sortino_ratio | -0.6797 |
| max_drawdown | 0.5776 |
| cagr | -0.2777 |
| net_avg_win | 58.7950 |
| net_avg_loss | -85.8710 |
| avg_hold_time_bars | 41.7420 |
| exposure | 0.7722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
