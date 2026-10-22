# EMA Hourly Continuation — GTC/USDT P21_144

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.7362 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8955 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -2.1016 |
| sortino_ratio | -0.6134 |
| max_drawdown | 0.5661 |
| cagr | -0.2457 |
| net_avg_win | 71.8849 |
| net_avg_loss | -85.4905 |
| avg_hold_time_bars | 25.7749 |
| exposure | 0.4944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
