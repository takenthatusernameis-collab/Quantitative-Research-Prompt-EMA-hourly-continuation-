# EMA Hourly Continuation — KAS/USDT P8_100

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.8516 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0390 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.0808 |
| sortino_ratio | -0.3424 |
| max_drawdown | 0.3386 |
| cagr | -0.1485 |
| net_avg_win | 76.2902 |
| net_avg_loss | -94.0971 |
| avg_hold_time_bars | 28.9201 |
| exposure | 0.6415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
