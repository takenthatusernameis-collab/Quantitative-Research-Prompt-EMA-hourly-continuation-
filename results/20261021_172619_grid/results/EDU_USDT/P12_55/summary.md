# EMA Hourly Continuation — EDU/USDT P12_55

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.7162 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9067 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.6488 |
| sortino_ratio | -1.0330 |
| max_drawdown | 0.7057 |
| cagr | -0.3788 |
| net_avg_win | 48.7393 |
| net_avg_loss | -63.4926 |
| avg_hold_time_bars | 10.2147 |
| exposure | 0.3467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
