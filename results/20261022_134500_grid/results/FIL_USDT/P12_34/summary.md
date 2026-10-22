# EMA Hourly Continuation — FIL/USDT P12_34

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1289 |
| net_profit_factor | 0.3779 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7935 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -9.8056 |
| sortino_ratio | -4.9644 |
| max_drawdown | 0.9981 |
| cagr | -0.9163 |
| net_avg_win | 10.8469 |
| net_avg_loss | -21.9777 |
| avg_hold_time_bars | 4.3856 |
| exposure | 0.2570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
