# EMA Hourly Continuation — THETA/USDT P20_89

**Symbol:** THETA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8028 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9933 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.5464 |
| sortino_ratio | -0.4852 |
| max_drawdown | 0.4890 |
| cagr | -0.2010 |
| net_avg_win | 73.3744 |
| net_avg_loss | -90.6420 |
| avg_hold_time_bars | 15.9333 |
| exposure | 0.3476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
