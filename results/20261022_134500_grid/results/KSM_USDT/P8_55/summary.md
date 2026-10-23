# EMA Hourly Continuation — KSM/USDT P8_55

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.5448 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8817 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -6.6309 |
| sortino_ratio | -2.9758 |
| max_drawdown | 0.9740 |
| cagr | -0.7644 |
| net_avg_win | 25.4417 |
| net_avg_loss | -37.6538 |
| avg_hold_time_bars | 10.7710 |
| exposure | 0.5023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
