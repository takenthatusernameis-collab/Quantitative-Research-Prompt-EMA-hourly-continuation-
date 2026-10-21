# EMA Hourly Continuation — GLM/USDT P21_100

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.6407 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8481 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -3.2906 |
| sortino_ratio | -1.0877 |
| max_drawdown | 0.7258 |
| cagr | -0.3946 |
| net_avg_win | 51.3008 |
| net_avg_loss | -68.0507 |
| avg_hold_time_bars | 16.8653 |
| exposure | 0.4155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
