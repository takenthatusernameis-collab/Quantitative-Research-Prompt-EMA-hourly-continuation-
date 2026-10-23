# EMA Hourly Continuation — REQ/USDT P20_89

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.5018 |
| net_win_rate | 0.4307 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -7.8139 |
| sortino_ratio | -3.2216 |
| max_drawdown | 0.9831 |
| cagr | -0.8008 |
| net_avg_win | 26.7450 |
| net_avg_loss | -40.3308 |
| avg_hold_time_bars | 10.3155 |
| exposure | 0.4028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
