# EMA Hourly Continuation — XEC/USDT P12_144

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.7617 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9684 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.8705 |
| sortino_ratio | -0.5736 |
| max_drawdown | 0.5434 |
| cagr | -0.2331 |
| net_avg_win | 68.1166 |
| net_avg_loss | -87.1470 |
| avg_hold_time_bars | 30.4267 |
| exposure | 0.6389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
