# EMA Hourly Continuation — ETC/USDT P89_100

**Symbol:** ETC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.1981 |
| net_win_rate | 0.3842 |
| gross_profit_factor | 0.7672 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -10.6716 |
| sortino_ratio | -3.9282 |
| max_drawdown | 0.9951 |
| cagr | -0.8792 |
| net_avg_win | 10.5027 |
| net_avg_loss | -33.0883 |
| avg_hold_time_bars | 2.2644 |
| exposure | 0.0627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
