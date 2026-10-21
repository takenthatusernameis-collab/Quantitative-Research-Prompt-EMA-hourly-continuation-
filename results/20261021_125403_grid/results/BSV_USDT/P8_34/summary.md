# EMA Hourly Continuation — BSV/USDT P8_34

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.6673 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9367 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.7986 |
| sortino_ratio | -1.4939 |
| max_drawdown | 0.8281 |
| cagr | -0.4949 |
| net_avg_win | 45.6856 |
| net_avg_loss | -62.2422 |
| avg_hold_time_bars | 8.2897 |
| exposure | 0.2849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
