# EMA Hourly Continuation — ICP/USDT P100_144

**Symbol:** ICP/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.8989 |
| net_win_rate | 0.5495 |
| gross_profit_factor | 1.2036 |
| gross_win_rate | 0.5495 |
| sharpe_ratio | -0.4143 |
| sortino_ratio | -0.0855 |
| max_drawdown | 0.1666 |
| cagr | -0.0403 |
| net_avg_win | 78.5766 |
| net_avg_loss | -106.6286 |
| avg_hold_time_bars | 6.7970 |
| exposure | 0.0624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
