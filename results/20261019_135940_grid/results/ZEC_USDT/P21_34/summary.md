# EMA Hourly Continuation — ZEC/USDT P21_34

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.2560 |
| net_win_rate | 0.4267 |
| gross_profit_factor | 0.7419 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -9.6056 |
| sortino_ratio | -4.3741 |
| max_drawdown | 0.9966 |
| cagr | -0.8950 |
| net_avg_win | 7.7045 |
| net_avg_loss | -22.3975 |
| avg_hold_time_bars | 2.5187 |
| exposure | 0.1194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
