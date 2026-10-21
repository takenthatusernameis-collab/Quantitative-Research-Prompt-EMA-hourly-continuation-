# EMA Hourly Continuation — JST/USDT P26_50

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.4600 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -4.8445 |
| sortino_ratio | -1.4801 |
| max_drawdown | 0.8276 |
| cagr | -0.4981 |
| net_avg_win | 32.6597 |
| net_avg_loss | -64.6818 |
| avg_hold_time_bars | 6.4479 |
| exposure | 0.1316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
