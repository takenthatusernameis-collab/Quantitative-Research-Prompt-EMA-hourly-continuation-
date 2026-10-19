# EMA Hourly Continuation — BCH/USDT P12_100

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.5906 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -5.3120 |
| sortino_ratio | -1.9471 |
| max_drawdown | 0.9159 |
| cagr | -0.6213 |
| net_avg_win | 40.5193 |
| net_avg_loss | -60.2597 |
| avg_hold_time_bars | 16.6950 |
| exposure | 0.5274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
