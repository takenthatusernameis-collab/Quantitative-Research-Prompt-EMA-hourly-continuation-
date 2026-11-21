# EMA Hourly Continuation — HTR/USDT P89_100

**Symbol:** HTR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.2474 |
| net_win_rate | 0.3277 |
| gross_profit_factor | 0.5771 |
| gross_win_rate | 0.3783 |
| sharpe_ratio | -10.5648 |
| sortino_ratio | -3.9108 |
| max_drawdown | 0.9944 |
| cagr | -0.8714 |
| net_avg_win | 15.2733 |
| net_avg_loss | -30.0922 |
| avg_hold_time_bars | 2.8959 |
| exposure | 0.0860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
