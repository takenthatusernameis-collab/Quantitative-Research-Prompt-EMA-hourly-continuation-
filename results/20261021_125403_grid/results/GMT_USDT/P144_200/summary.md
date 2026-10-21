# EMA Hourly Continuation — GMT/USDT P144_200

**Symbol:** GMT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.7615 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0239 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.1662 |
| sortino_ratio | -0.2419 |
| max_drawdown | 0.2762 |
| cagr | -0.1051 |
| net_avg_win | 73.2848 |
| net_avg_loss | -100.0150 |
| avg_hold_time_bars | 6.8413 |
| exposure | 0.0647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
