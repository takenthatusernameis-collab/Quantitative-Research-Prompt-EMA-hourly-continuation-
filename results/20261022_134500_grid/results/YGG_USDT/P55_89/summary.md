# EMA Hourly Continuation — YGG/USDT P55_89

**Symbol:** YGG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.5888 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -4.4829 |
| sortino_ratio | -1.6454 |
| max_drawdown | 0.8705 |
| cagr | -0.5456 |
| net_avg_win | 37.3500 |
| net_avg_loss | -60.6807 |
| avg_hold_time_bars | 4.1802 |
| exposure | 0.1281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
