# EMA Hourly Continuation — MLK/USDT P144_200

**Symbol:** MLK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.4065 |
| net_win_rate | 0.3538 |
| gross_profit_factor | 0.5947 |
| gross_win_rate | 0.3538 |
| sharpe_ratio | -4.1306 |
| sortino_ratio | -0.8174 |
| max_drawdown | 0.6249 |
| cagr | -0.3221 |
| net_avg_win | 62.0371 |
| net_avg_loss | -83.5677 |
| avg_hold_time_bars | 9.2615 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
