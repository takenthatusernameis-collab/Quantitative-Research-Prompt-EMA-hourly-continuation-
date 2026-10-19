# EMA Hourly Continuation — TRX/USDT P50_200

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.3446 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 1.0156 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -6.0064 |
| sortino_ratio | -1.6507 |
| max_drawdown | 0.8906 |
| cagr | -0.5841 |
| net_avg_win | 28.1743 |
| net_avg_loss | -62.5467 |
| avg_hold_time_bars | 18.0183 |
| exposure | 0.3137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
