# EMA Hourly Continuation — MOG/USDT P8_100

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.8841 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -0.8710 |
| sortino_ratio | -0.2773 |
| max_drawdown | 0.3844 |
| cagr | -0.1238 |
| net_avg_win | 87.9867 |
| net_avg_loss | -100.4005 |
| avg_hold_time_bars | 28.4580 |
| exposure | 0.6394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
