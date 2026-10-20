# EMA Hourly Continuation — VR/USDT P20_89

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.4487 |
| net_win_rate | 0.3411 |
| gross_profit_factor | 0.6662 |
| gross_win_rate | 0.3522 |
| sharpe_ratio | -10.6289 |
| sortino_ratio | -4.2048 |
| max_drawdown | 0.9975 |
| cagr | -0.9072 |
| net_avg_win | 29.3087 |
| net_avg_loss | -33.8186 |
| avg_hold_time_bars | 10.2155 |
| exposure | 0.3770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
