# EMA Hourly Continuation — KCS/USDT P26_55

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.3353 |
| net_win_rate | 0.3810 |
| gross_profit_factor | 0.6696 |
| gross_win_rate | 0.3833 |
| sharpe_ratio | -6.9835 |
| sortino_ratio | -2.0853 |
| max_drawdown | 0.9165 |
| cagr | -0.6268 |
| net_avg_win | 28.8692 |
| net_avg_loss | -52.9914 |
| avg_hold_time_bars | 7.5214 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
