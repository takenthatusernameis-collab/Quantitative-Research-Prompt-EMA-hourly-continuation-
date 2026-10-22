# EMA Hourly Continuation — RAY/USDT P8_89

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.6700 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9390 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -3.6434 |
| sortino_ratio | -1.4130 |
| max_drawdown | 0.8315 |
| cagr | -0.4926 |
| net_avg_win | 45.2589 |
| net_avg_loss | -62.2861 |
| avg_hold_time_bars | 17.4693 |
| exposure | 0.6075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
