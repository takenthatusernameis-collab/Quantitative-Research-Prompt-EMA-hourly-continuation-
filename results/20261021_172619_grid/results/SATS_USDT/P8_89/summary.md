# EMA Hourly Continuation — SATS/USDT P8_89

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.8026 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9544 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -1.7040 |
| sortino_ratio | -0.5664 |
| max_drawdown | 0.5188 |
| cagr | -0.2310 |
| net_avg_win | 74.3238 |
| net_avg_loss | -87.6448 |
| avg_hold_time_bars | 24.1193 |
| exposure | 0.5948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
