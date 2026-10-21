# EMA Hourly Continuation — 1INCH/USDT P50_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -2.5264 |
| sortino_ratio | -0.7073 |
| max_drawdown | 0.5827 |
| cagr | -0.2760 |
| net_avg_win | 62.9517 |
| net_avg_loss | -87.7690 |
| avg_hold_time_bars | 7.3753 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
