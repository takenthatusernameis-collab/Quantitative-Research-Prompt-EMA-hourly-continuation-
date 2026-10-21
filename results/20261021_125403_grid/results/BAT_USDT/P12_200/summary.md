# EMA Hourly Continuation — BAT/USDT P12_200

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8790 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0720 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -0.6435 |
| sortino_ratio | -0.1605 |
| max_drawdown | 0.2851 |
| cagr | -0.0734 |
| net_avg_win | 81.1664 |
| net_avg_loss | -99.3466 |
| avg_hold_time_bars | 54.3322 |
| exposure | 0.7434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
