# EMA Hourly Continuation — AVAX/USDT P21_89

**Symbol:** AVAX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6691 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -4.3855 |
| sortino_ratio | -1.6067 |
| max_drawdown | 0.8681 |
| cagr | -0.5432 |
| net_avg_win | 52.7072 |
| net_avg_loss | -73.0215 |
| avg_hold_time_bars | 11.1166 |
| exposure | 0.3466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
