# EMA Hourly Continuation — ARPA/USDT P21_100

**Symbol:** ARPA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7085 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -2.7118 |
| sortino_ratio | -0.9110 |
| max_drawdown | 0.6891 |
| cagr | -0.3414 |
| net_avg_win | 59.0722 |
| net_avg_loss | -77.5864 |
| avg_hold_time_bars | 15.6169 |
| exposure | 0.3929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
