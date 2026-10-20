# EMA Hourly Continuation — T/USDT P8_34

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.5803 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 1.0158 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -6.5905 |
| sortino_ratio | -2.9939 |
| max_drawdown | 0.9750 |
| cagr | -0.7676 |
| net_avg_win | 27.3411 |
| net_avg_loss | -41.2562 |
| avg_hold_time_bars | 7.3788 |
| exposure | 0.3526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
