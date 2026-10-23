# EMA Hourly Continuation — VR/USDT P144_200

**Symbol:** VR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.3707 |
| net_win_rate | 0.2734 |
| gross_profit_factor | 0.6226 |
| gross_win_rate | 0.2871 |
| sharpe_ratio | -10.6099 |
| sortino_ratio | -3.4856 |
| max_drawdown | 0.9932 |
| cagr | -0.8610 |
| net_avg_win | 41.7774 |
| net_avg_loss | -42.4150 |
| avg_hold_time_bars | 4.7871 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
