# EMA Hourly Continuation — BONK/USDT P12_26

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8755 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1148 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -0.8836 |
| sortino_ratio | -0.2587 |
| max_drawdown | 0.3857 |
| cagr | -0.1148 |
| net_avg_win | 85.4425 |
| net_avg_loss | -108.6054 |
| avg_hold_time_bars | 5.7476 |
| exposure | 0.1076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
