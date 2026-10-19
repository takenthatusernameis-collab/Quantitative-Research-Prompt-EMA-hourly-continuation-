# EMA Hourly Continuation — POL/USDT P144_200

**Symbol:** POL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.3449 |
| net_win_rate | 0.3995 |
| gross_profit_factor | 0.6393 |
| gross_win_rate | 0.4069 |
| sharpe_ratio | -6.0772 |
| sortino_ratio | -1.7258 |
| max_drawdown | 0.8914 |
| cagr | -0.5794 |
| net_avg_win | 28.9820 |
| net_avg_loss | -55.9105 |
| avg_hold_time_bars | 4.7419 |
| exposure | 0.0869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
