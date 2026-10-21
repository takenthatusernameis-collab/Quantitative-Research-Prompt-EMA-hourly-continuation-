# EMA Hourly Continuation — ADA/USDT P21_34

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.7035 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.8273 |
| sortino_ratio | -0.4271 |
| max_drawdown | 0.4104 |
| cagr | -0.1768 |
| net_avg_win | 69.4646 |
| net_avg_loss | -98.7445 |
| avg_hold_time_bars | 5.1288 |
| exposure | 0.0615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
