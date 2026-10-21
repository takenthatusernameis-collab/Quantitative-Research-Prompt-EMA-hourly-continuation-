# EMA Hourly Continuation — ETN/USDT P21_144

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.5578 |
| net_win_rate | 0.4039 |
| gross_profit_factor | 0.6771 |
| gross_win_rate | 0.4039 |
| sharpe_ratio | -3.8037 |
| sortino_ratio | -1.1087 |
| max_drawdown | 0.6748 |
| cagr | -0.4010 |
| net_avg_win | 57.3585 |
| net_avg_loss | -69.6770 |
| avg_hold_time_bars | 21.7549 |
| exposure | 0.4242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
