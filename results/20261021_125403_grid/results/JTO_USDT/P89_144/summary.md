# EMA Hourly Continuation — JTO/USDT P89_144

**Symbol:** JTO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.6124 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7749 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -2.5866 |
| sortino_ratio | -0.6202 |
| max_drawdown | 0.5228 |
| cagr | -0.2482 |
| net_avg_win | 64.6584 |
| net_avg_loss | -81.9682 |
| avg_hold_time_bars | 6.9650 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
