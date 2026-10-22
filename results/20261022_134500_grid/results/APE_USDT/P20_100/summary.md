# EMA Hourly Continuation — APE/USDT P20_100

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.6357 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9356 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -3.5286 |
| sortino_ratio | -1.3065 |
| max_drawdown | 0.8025 |
| cagr | -0.4584 |
| net_avg_win | 41.4161 |
| net_avg_loss | -61.0907 |
| avg_hold_time_bars | 12.6564 |
| exposure | 0.3935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
