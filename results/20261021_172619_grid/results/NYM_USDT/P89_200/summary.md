# EMA Hourly Continuation — NYM/USDT P89_200

**Symbol:** NYM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.4718 |
| net_win_rate | 0.4100 |
| gross_profit_factor | 0.7090 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -3.4910 |
| sortino_ratio | -0.7663 |
| max_drawdown | 0.6008 |
| cagr | -0.3019 |
| net_avg_win | 54.1906 |
| net_avg_loss | -79.8262 |
| avg_hold_time_bars | 16.7197 |
| exposure | 0.1816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
