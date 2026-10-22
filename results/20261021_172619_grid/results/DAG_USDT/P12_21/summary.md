# EMA Hourly Continuation — DAG/USDT P12_21

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.4850 |
| net_win_rate | 0.3936 |
| gross_profit_factor | 0.6156 |
| gross_win_rate | 0.3936 |
| sharpe_ratio | -2.8669 |
| sortino_ratio | -0.5543 |
| max_drawdown | 0.4929 |
| cagr | -0.2265 |
| net_avg_win | 60.4898 |
| net_avg_loss | -80.9547 |
| avg_hold_time_bars | 6.2287 |
| exposure | 0.0532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
