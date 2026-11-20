# EMA Hourly Continuation — P2P/USDT P12_34

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.3561 |
| net_win_rate | 0.3443 |
| gross_profit_factor | 0.5744 |
| gross_win_rate | 0.3468 |
| sharpe_ratio | -10.7447 |
| sortino_ratio | -5.1754 |
| max_drawdown | 0.9984 |
| cagr | -0.9234 |
| net_avg_win | 13.5348 |
| net_avg_loss | -19.9568 |
| avg_hold_time_bars | 5.1477 |
| exposure | 0.2773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
