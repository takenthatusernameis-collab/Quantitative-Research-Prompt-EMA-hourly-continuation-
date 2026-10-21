# EMA Hourly Continuation — SUPER/USDT P8_26

**Symbol:** SUPER/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.8545 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.1647 |
| gross_win_rate | 0.5415 |
| sharpe_ratio | -1.3324 |
| sortino_ratio | -0.5124 |
| max_drawdown | 0.5054 |
| cagr | -0.2131 |
| net_avg_win | 69.5375 |
| net_avg_loss | -94.4849 |
| avg_hold_time_bars | 6.5316 |
| exposure | 0.2111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
