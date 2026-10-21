# EMA Hourly Continuation — BCH/USDT P12_50

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.7393 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0376 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -2.2620 |
| sortino_ratio | -0.7827 |
| max_drawdown | 0.5934 |
| cagr | -0.3012 |
| net_avg_win | 56.8497 |
| net_avg_loss | -80.4303 |
| avg_hold_time_bars | 11.1244 |
| exposure | 0.2928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
