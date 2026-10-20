# EMA Hourly Continuation — BIGTIME/USDT P20_50

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.5900 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -5.1906 |
| sortino_ratio | -2.2354 |
| max_drawdown | 0.9325 |
| cagr | -0.6544 |
| net_avg_win | 30.0510 |
| net_avg_loss | -46.7432 |
| avg_hold_time_bars | 6.0858 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
