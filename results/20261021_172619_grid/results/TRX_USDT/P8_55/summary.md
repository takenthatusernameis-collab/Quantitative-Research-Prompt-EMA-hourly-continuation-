# EMA Hourly Continuation — TRX/USDT P8_55

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.5734 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 1.0292 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -4.8852 |
| sortino_ratio | -1.7445 |
| max_drawdown | 0.8727 |
| cagr | -0.5517 |
| net_avg_win | 38.3167 |
| net_avg_loss | -66.1731 |
| avg_hold_time_bars | 15.9656 |
| exposure | 0.4434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
