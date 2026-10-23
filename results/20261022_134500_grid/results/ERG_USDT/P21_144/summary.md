# EMA Hourly Continuation — ERG/USDT P21_144

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.4822 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.7115 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -4.9577 |
| sortino_ratio | -1.6897 |
| max_drawdown | 0.8708 |
| cagr | -0.5532 |
| net_avg_win | 32.1993 |
| net_avg_loss | -50.3286 |
| avg_hold_time_bars | 18.2003 |
| exposure | 0.4831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
