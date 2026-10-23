# EMA Hourly Continuation — KNC/USDT P12_20

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1355 |
| net_profit_factor | 0.2811 |
| net_win_rate | 0.3779 |
| gross_profit_factor | 0.7953 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -13.9825 |
| sortino_ratio | -7.3981 |
| max_drawdown | 0.9999 |
| cagr | -0.9784 |
| net_avg_win | 7.6373 |
| net_avg_loss | -16.5002 |
| avg_hold_time_bars | 3.1963 |
| exposure | 0.1969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
