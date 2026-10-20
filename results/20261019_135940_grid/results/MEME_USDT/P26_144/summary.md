# EMA Hourly Continuation — MEME/USDT P26_144

**Symbol:** MEME/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7286 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9857 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.1307 |
| sortino_ratio | -0.6439 |
| max_drawdown | 0.5642 |
| cagr | -0.2627 |
| net_avg_win | 63.5148 |
| net_avg_loss | -85.2912 |
| avg_hold_time_bars | 24.7199 |
| exposure | 0.5135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
