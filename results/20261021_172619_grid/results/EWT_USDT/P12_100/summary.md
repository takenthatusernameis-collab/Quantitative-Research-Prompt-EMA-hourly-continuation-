# EMA Hourly Continuation — EWT/USDT P12_100

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6388 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.7805 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -3.0133 |
| sortino_ratio | -0.9557 |
| max_drawdown | 0.7031 |
| cagr | -0.3568 |
| net_avg_win | 53.1176 |
| net_avg_loss | -66.4648 |
| avg_hold_time_bars | 18.3586 |
| exposure | 0.4189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
