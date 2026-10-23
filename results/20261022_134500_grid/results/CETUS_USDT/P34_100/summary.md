# EMA Hourly Continuation — CETUS/USDT P34_100

**Symbol:** CETUS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.7037 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 1.0167 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -3.0738 |
| sortino_ratio | -1.0885 |
| max_drawdown | 0.7346 |
| cagr | -0.4011 |
| net_avg_win | 55.7609 |
| net_avg_loss | -77.2417 |
| avg_hold_time_bars | 10.3163 |
| exposure | 0.2922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
