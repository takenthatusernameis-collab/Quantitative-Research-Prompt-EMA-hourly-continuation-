# EMA Hourly Continuation — VR/USDT P26_200

**Symbol:** VR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.4555 |
| net_win_rate | 0.3194 |
| gross_profit_factor | 0.6804 |
| gross_win_rate | 0.3353 |
| sharpe_ratio | -8.7436 |
| sortino_ratio | -2.7242 |
| max_drawdown | 0.9810 |
| cagr | -0.7924 |
| net_avg_win | 51.2660 |
| net_avg_loss | -52.8142 |
| avg_hold_time_bars | 25.5210 |
| exposure | 0.5812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
