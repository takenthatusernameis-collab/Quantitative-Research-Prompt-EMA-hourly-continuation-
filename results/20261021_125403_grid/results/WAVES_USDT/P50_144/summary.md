# EMA Hourly Continuation — WAVES/USDT P50_144

**Symbol:** WAVES/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.7157 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -1.9876 |
| sortino_ratio | -0.5609 |
| max_drawdown | 0.5111 |
| cagr | -0.2278 |
| net_avg_win | 62.6173 |
| net_avg_loss | -85.2704 |
| avg_hold_time_bars | 14.6787 |
| exposure | 0.2595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
