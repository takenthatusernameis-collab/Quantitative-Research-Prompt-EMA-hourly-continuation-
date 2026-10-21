# EMA Hourly Continuation — DOT/USDT P89_100

**Symbol:** DOT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 74 |
| net_profit_factor | 0.5643 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8483 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -1.4879 |
| sortino_ratio | -0.1834 |
| max_drawdown | 0.2341 |
| cagr | -0.0808 |
| net_avg_win | 72.6062 |
| net_avg_loss | -109.3710 |
| avg_hold_time_bars | 4.7973 |
| exposure | 0.0161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
