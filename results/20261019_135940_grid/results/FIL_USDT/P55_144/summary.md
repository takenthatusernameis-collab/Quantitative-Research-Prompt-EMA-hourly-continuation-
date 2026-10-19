# EMA Hourly Continuation — FIL/USDT P55_144

**Symbol:** FIL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.5333 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8809 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -4.3500 |
| sortino_ratio | -1.3458 |
| max_drawdown | 0.8069 |
| cagr | -0.4733 |
| net_avg_win | 41.9402 |
| net_avg_loss | -66.1948 |
| avg_hold_time_bars | 10.0231 |
| exposure | 0.2173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
