# EMA Hourly Continuation — T/USDT P12_34

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6691 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -3.7458 |
| sortino_ratio | -1.4057 |
| max_drawdown | 0.8111 |
| cagr | -0.4733 |
| net_avg_win | 48.3741 |
| net_avg_loss | -68.8086 |
| avg_hold_time_bars | 7.8326 |
| exposure | 0.2435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
