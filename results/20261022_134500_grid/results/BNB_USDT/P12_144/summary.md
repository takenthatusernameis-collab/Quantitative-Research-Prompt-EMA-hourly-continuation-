# EMA Hourly Continuation — BNB/USDT P12_144

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.3549 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8397 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -6.5118 |
| sortino_ratio | -2.1522 |
| max_drawdown | 0.9403 |
| cagr | -0.6697 |
| net_avg_win | 21.2402 |
| net_avg_loss | -45.8742 |
| avg_hold_time_bars | 25.0768 |
| exposure | 0.6383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
