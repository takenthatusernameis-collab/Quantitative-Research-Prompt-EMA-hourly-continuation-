# EMA Hourly Continuation — ACE/USDT P12_26

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.4423 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -7.4877 |
| sortino_ratio | -3.4291 |
| max_drawdown | 0.9847 |
| cagr | -0.8077 |
| net_avg_win | 16.5779 |
| net_avg_loss | -30.5925 |
| avg_hold_time_bars | 4.6746 |
| exposure | 0.2217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
