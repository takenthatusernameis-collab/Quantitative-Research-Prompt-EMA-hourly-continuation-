# EMA Hourly Continuation — SAFE/USDT P12_34

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.4386 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.7878 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -7.8499 |
| sortino_ratio | -3.8659 |
| max_drawdown | 0.9910 |
| cagr | -0.8460 |
| net_avg_win | 14.2764 |
| net_avg_loss | -26.5715 |
| avg_hold_time_bars | 4.9876 |
| exposure | 0.2755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
