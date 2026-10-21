# EMA Hourly Continuation — AR/USDT P34_55

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7971 |
| net_win_rate | 0.5224 |
| gross_profit_factor | 1.0575 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | -1.1198 |
| sortino_ratio | -0.2954 |
| max_drawdown | 0.3222 |
| cagr | -0.1274 |
| net_avg_win | 65.0883 |
| net_avg_loss | -89.3093 |
| avg_hold_time_bars | 5.9612 |
| exposure | 0.0908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
