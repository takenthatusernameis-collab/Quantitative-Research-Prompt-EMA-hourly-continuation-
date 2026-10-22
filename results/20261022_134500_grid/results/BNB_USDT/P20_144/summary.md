# EMA Hourly Continuation — BNB/USDT P20_144

**Symbol:** BNB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.3755 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8659 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -6.5563 |
| sortino_ratio | -2.1605 |
| max_drawdown | 0.9434 |
| cagr | -0.6779 |
| net_avg_win | 22.6505 |
| net_avg_loss | -48.8063 |
| avg_hold_time_bars | 20.9750 |
| exposure | 0.5330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
