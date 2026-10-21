# EMA Hourly Continuation — API3/USDT P21_144

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7857 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9462 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.5625 |
| sortino_ratio | -0.4497 |
| max_drawdown | 0.4591 |
| cagr | -0.1877 |
| net_avg_win | 75.3239 |
| net_avg_loss | -90.8184 |
| avg_hold_time_bars | 28.6020 |
| exposure | 0.5291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
