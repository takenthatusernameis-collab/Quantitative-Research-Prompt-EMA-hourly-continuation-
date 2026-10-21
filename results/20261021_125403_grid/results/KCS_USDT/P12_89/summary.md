# EMA Hourly Continuation — KCS/USDT P12_89

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5398 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -4.4849 |
| sortino_ratio | -1.4362 |
| max_drawdown | 0.8202 |
| cagr | -0.4856 |
| net_avg_win | 41.9470 |
| net_avg_loss | -64.6108 |
| avg_hold_time_bars | 22.1860 |
| exposure | 0.5042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
