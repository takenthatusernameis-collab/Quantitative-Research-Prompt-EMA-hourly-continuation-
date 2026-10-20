# EMA Hourly Continuation — DIA/USDT P26_55

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 886 |
| net_profit_factor | 0.4545 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.7862 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -7.3794 |
| sortino_ratio | -3.0774 |
| max_drawdown | 0.9788 |
| cagr | -0.7810 |
| net_avg_win | 21.2231 |
| net_avg_loss | -35.7228 |
| avg_hold_time_bars | 5.0079 |
| exposure | 0.2008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
