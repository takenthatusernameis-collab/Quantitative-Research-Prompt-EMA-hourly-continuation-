# EMA Hourly Continuation — NMR/USDT P50_144

**Symbol:** NMR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6039 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -3.9126 |
| sortino_ratio | -1.2837 |
| max_drawdown | 0.7916 |
| cagr | -0.4572 |
| net_avg_win | 47.0763 |
| net_avg_loss | -69.2349 |
| avg_hold_time_bars | 11.0481 |
| exposure | 0.2712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
