# EMA Hourly Continuation — YFI/USDT P50_144

**Symbol:** YFI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6606 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.7953 |
| sortino_ratio | -0.8146 |
| max_drawdown | 0.6355 |
| cagr | -0.3116 |
| net_avg_win | 59.3874 |
| net_avg_loss | -82.8530 |
| avg_hold_time_bars | 15.4772 |
| exposure | 0.2920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
