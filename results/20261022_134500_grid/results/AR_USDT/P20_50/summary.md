# EMA Hourly Continuation — AR/USDT P20_50

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.4397 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.7006 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -7.4149 |
| sortino_ratio | -3.3247 |
| max_drawdown | 0.9830 |
| cagr | -0.8025 |
| net_avg_win | 17.5704 |
| net_avg_loss | -30.2990 |
| avg_hold_time_bars | 4.5354 |
| exposure | 0.2099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
