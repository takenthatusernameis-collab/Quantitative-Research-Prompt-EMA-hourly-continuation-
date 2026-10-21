# EMA Hourly Continuation — BABYDOGE/USDT P12_21

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 12 |
| net_profit_factor | 1.2896 |
| net_win_rate | 0.5833 |
| gross_profit_factor | 1.3916 |
| gross_win_rate | 0.5833 |
| sharpe_ratio | 0.2817 |
| sortino_ratio | 0.0144 |
| max_drawdown | 0.0218 |
| cagr | 0.0059 |
| net_avg_win | 95.3224 |
| net_avg_loss | -103.4856 |
| avg_hold_time_bars | 5.4167 |
| exposure | 0.0029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
