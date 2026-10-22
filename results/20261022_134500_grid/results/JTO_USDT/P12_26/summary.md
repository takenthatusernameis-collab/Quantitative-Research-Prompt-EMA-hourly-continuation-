# EMA Hourly Continuation — JTO/USDT P12_26

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1388 |
| net_profit_factor | 0.5495 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 1.0218 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -8.0578 |
| sortino_ratio | -4.2225 |
| max_drawdown | 0.9946 |
| cagr | -0.8722 |
| net_avg_win | 19.0116 |
| net_avg_loss | -29.4298 |
| avg_hold_time_bars | 3.2831 |
| exposure | 0.2071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
