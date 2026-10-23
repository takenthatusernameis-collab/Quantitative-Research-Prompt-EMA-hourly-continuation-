# EMA Hourly Continuation — ACE/USDT P20_26

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.2841 |
| net_win_rate | 0.4149 |
| gross_profit_factor | 0.8642 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -9.5515 |
| sortino_ratio | -4.1474 |
| max_drawdown | 0.9947 |
| cagr | -0.8733 |
| net_avg_win | 10.2533 |
| net_avg_loss | -25.5856 |
| avg_hold_time_bars | 3.3567 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
