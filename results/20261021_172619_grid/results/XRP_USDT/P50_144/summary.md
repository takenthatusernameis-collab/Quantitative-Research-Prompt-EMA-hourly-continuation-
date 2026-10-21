# EMA Hourly Continuation — XRP/USDT P50_144

**Symbol:** XRP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.5235 |
| gross_profit_factor | 1.0838 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -1.4709 |
| sortino_ratio | -0.3785 |
| max_drawdown | 0.3956 |
| cagr | -0.1595 |
| net_avg_win | 65.1275 |
| net_avg_loss | -94.8172 |
| avg_hold_time_bars | 17.8213 |
| exposure | 0.2584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
