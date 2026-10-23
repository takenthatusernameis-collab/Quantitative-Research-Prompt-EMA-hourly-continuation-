# EMA Hourly Continuation — WIN/USDT P50_55

**Symbol:** WIN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.1155 |
| net_win_rate | 0.2821 |
| gross_profit_factor | 0.6571 |
| gross_win_rate | 0.3667 |
| sharpe_ratio | -14.9964 |
| sortino_ratio | -6.5756 |
| max_drawdown | 0.9999 |
| cagr | -0.9769 |
| net_avg_win | 5.9322 |
| net_avg_loss | -20.1863 |
| avg_hold_time_bars | 1.9000 |
| exposure | 0.0674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
