# EMA Hourly Continuation — UMA/USDT P12_20

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.5607 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8809 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -3.5959 |
| sortino_ratio | -1.0863 |
| max_drawdown | 0.7284 |
| cagr | -0.3937 |
| net_avg_win | 42.8734 |
| net_avg_loss | -70.2000 |
| avg_hold_time_bars | 5.0989 |
| exposure | 0.1031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
