# EMA Hourly Continuation — DOT/USDT P8_34

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.7169 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.8832 |
| sortino_ratio | -1.0976 |
| max_drawdown | 0.7357 |
| cagr | -0.3942 |
| net_avg_win | 52.4007 |
| net_avg_loss | -70.2496 |
| avg_hold_time_bars | 8.8598 |
| exposure | 0.2843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
