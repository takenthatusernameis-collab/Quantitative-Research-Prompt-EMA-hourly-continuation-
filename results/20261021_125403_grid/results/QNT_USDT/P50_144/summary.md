# EMA Hourly Continuation — QNT/USDT P50_144

**Symbol:** QNT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7044 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9558 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.2435 |
| sortino_ratio | -0.6569 |
| max_drawdown | 0.5529 |
| cagr | -0.2597 |
| net_avg_win | 61.6160 |
| net_avg_loss | -84.1840 |
| avg_hold_time_bars | 12.5742 |
| exposure | 0.2389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
