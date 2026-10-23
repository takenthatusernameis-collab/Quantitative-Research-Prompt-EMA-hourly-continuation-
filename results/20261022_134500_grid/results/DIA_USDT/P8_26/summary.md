# EMA Hourly Continuation — DIA/USDT P8_26

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1423 |
| net_profit_factor | 0.3792 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.7457 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -9.0264 |
| sortino_ratio | -4.7677 |
| max_drawdown | 0.9974 |
| cagr | -0.9049 |
| net_avg_win | 9.6254 |
| net_avg_loss | -20.3373 |
| avg_hold_time_bars | 4.4877 |
| exposure | 0.2890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
