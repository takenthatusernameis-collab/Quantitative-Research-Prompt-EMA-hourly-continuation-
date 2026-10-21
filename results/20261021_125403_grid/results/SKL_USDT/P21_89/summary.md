# EMA Hourly Continuation — SKL/USDT P21_89

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.7590 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.8999 |
| sortino_ratio | -0.6045 |
| max_drawdown | 0.5325 |
| cagr | -0.2428 |
| net_avg_win | 65.4141 |
| net_avg_loss | -82.1144 |
| avg_hold_time_bars | 16.6069 |
| exposure | 0.3744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
