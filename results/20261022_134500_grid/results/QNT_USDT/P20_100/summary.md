# EMA Hourly Continuation — QNT/USDT P20_100

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 826 |
| net_profit_factor | 0.5514 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -5.2493 |
| sortino_ratio | -2.1159 |
| max_drawdown | 0.9289 |
| cagr | -0.6445 |
| net_avg_win | 28.5863 |
| net_avg_loss | -48.2072 |
| avg_hold_time_bars | 10.2094 |
| exposure | 0.3833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
