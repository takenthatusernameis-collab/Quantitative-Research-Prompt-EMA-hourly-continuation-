# EMA Hourly Continuation — RAY/USDT P20_55

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9560 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.3866 |
| sortino_ratio | -0.7785 |
| max_drawdown | 0.6662 |
| cagr | -0.3015 |
| net_avg_win | 72.3474 |
| net_avg_loss | -88.5955 |
| avg_hold_time_bars | 8.7094 |
| exposure | 0.2070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
