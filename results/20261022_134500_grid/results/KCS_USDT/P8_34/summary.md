# EMA Hourly Continuation — KCS/USDT P8_34

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1342 |
| net_profit_factor | 0.2137 |
| net_win_rate | 0.3167 |
| gross_profit_factor | 0.7037 |
| gross_win_rate | 0.3949 |
| sharpe_ratio | -16.8000 |
| sortino_ratio | -9.0382 |
| max_drawdown | 1.0000 |
| cagr | -0.9926 |
| net_avg_win | 6.3937 |
| net_avg_loss | -13.8684 |
| avg_hold_time_bars | 5.9978 |
| exposure | 0.3659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
