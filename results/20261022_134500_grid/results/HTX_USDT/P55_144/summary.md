# EMA Hourly Continuation — HTX/USDT P55_144

**Symbol:** HTX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.2885 |
| net_win_rate | 0.3086 |
| gross_profit_factor | 0.7361 |
| gross_win_rate | 0.3741 |
| sharpe_ratio | -10.5891 |
| sortino_ratio | -3.7283 |
| max_drawdown | 0.9935 |
| cagr | -0.8621 |
| net_avg_win | 22.5036 |
| net_avg_loss | -34.8145 |
| avg_hold_time_bars | 10.8621 |
| exposure | 0.2851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
