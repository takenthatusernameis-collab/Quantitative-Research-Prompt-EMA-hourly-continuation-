# EMA Hourly Continuation — CTC/USDT P12_26

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1372 |
| net_profit_factor | 0.3274 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -11.4883 |
| sortino_ratio | -6.0016 |
| max_drawdown | 0.9996 |
| cagr | -0.9546 |
| net_avg_win | 8.3593 |
| net_avg_loss | -18.8112 |
| avg_hold_time_bars | 3.6545 |
| exposure | 0.2279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
