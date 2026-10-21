# EMA Hourly Continuation — ALGO/USDT P8_144

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.9478 |
| net_win_rate | 0.5292 |
| gross_profit_factor | 1.1060 |
| gross_win_rate | 0.5292 |
| sharpe_ratio | -0.2210 |
| sortino_ratio | -0.0527 |
| max_drawdown | 0.1521 |
| cagr | -0.0281 |
| net_avg_win | 86.5722 |
| net_avg_loss | -102.6666 |
| avg_hold_time_bars | 64.1898 |
| exposure | 0.7995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
