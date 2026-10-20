# EMA Hourly Continuation — WAVES/USDT P89_100

**Symbol:** WAVES/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.1985 |
| net_win_rate | 0.3182 |
| gross_profit_factor | 0.6307 |
| gross_win_rate | 0.3821 |
| sharpe_ratio | -12.4361 |
| sortino_ratio | -4.9419 |
| max_drawdown | 0.9989 |
| cagr | -0.9331 |
| net_avg_win | 11.0414 |
| net_avg_loss | -25.9626 |
| avg_hold_time_bars | 2.5241 |
| exposure | 0.0808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
