# EMA Hourly Continuation — TRX/USDT P20_89

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.3299 |
| net_win_rate | 0.4104 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -9.1275 |
| sortino_ratio | -3.3254 |
| max_drawdown | 0.9890 |
| cagr | -0.8339 |
| net_avg_win | 18.1652 |
| net_avg_loss | -38.3327 |
| avg_hold_time_bars | 11.9877 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
