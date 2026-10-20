# EMA Hourly Continuation — ANKR/USDT P12_34

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1190 |
| net_profit_factor | 0.4518 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.8752 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -9.7388 |
| sortino_ratio | -4.7515 |
| max_drawdown | 0.9974 |
| cagr | -0.9062 |
| net_avg_win | 16.3439 |
| net_avg_loss | -26.4844 |
| avg_hold_time_bars | 5.9613 |
| exposure | 0.3225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
