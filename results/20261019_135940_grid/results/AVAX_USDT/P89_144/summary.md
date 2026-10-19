# EMA Hourly Continuation — AVAX/USDT P89_144

**Symbol:** AVAX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.4491 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -5.6083 |
| sortino_ratio | -1.7016 |
| max_drawdown | 0.8896 |
| cagr | -0.5785 |
| net_avg_win | 34.8787 |
| net_avg_loss | -61.3662 |
| avg_hold_time_bars | 4.6674 |
| exposure | 0.0995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
