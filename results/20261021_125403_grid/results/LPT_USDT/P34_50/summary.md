# EMA Hourly Continuation — LPT/USDT P34_50

**Symbol:** LPT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.7710 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -3.9212 |
| sortino_ratio | -1.0483 |
| max_drawdown | 0.7088 |
| cagr | -0.3846 |
| net_avg_win | 53.4054 |
| net_avg_loss | -75.5472 |
| avg_hold_time_bars | 5.3903 |
| exposure | 0.0860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
