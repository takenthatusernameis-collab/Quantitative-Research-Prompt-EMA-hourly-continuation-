# EMA Hourly Continuation — RSR/USDT P8_34

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.3909 |
| sortino_ratio | -0.9259 |
| max_drawdown | 0.6830 |
| cagr | -0.3469 |
| net_avg_win | 56.4487 |
| net_avg_loss | -71.2198 |
| avg_hold_time_bars | 9.2425 |
| exposure | 0.3084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
