# EMA Hourly Continuation — BONK/USDT P89_144

**Symbol:** BONK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.7354 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -1.4281 |
| sortino_ratio | -0.3276 |
| max_drawdown | 0.3806 |
| cagr | -0.1403 |
| net_avg_win | 70.2492 |
| net_avg_loss | -89.7755 |
| avg_hold_time_bars | 9.7558 |
| exposure | 0.1144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
