# EMA Hourly Continuation — AXL/USDT P8_144

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6834 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.9459 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -3.5445 |
| sortino_ratio | -1.2301 |
| max_drawdown | 0.7835 |
| cagr | -0.4436 |
| net_avg_win | 58.4788 |
| net_avg_loss | -73.9018 |
| avg_hold_time_bars | 25.7837 |
| exposure | 0.7175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
