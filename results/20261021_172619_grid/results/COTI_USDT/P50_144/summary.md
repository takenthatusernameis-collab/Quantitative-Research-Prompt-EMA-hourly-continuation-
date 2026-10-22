# EMA Hourly Continuation — COTI/USDT P50_144

**Symbol:** COTI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8727 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0657 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.6480 |
| sortino_ratio | -0.1757 |
| max_drawdown | 0.3378 |
| cagr | -0.0808 |
| net_avg_win | 70.6778 |
| net_avg_loss | -88.6540 |
| avg_hold_time_bars | 15.9435 |
| exposure | 0.2565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
