# EMA Hourly Continuation — YFI/USDT P12_34

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.5511 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -4.9344 |
| sortino_ratio | -1.8896 |
| max_drawdown | 0.8884 |
| cagr | -0.5792 |
| net_avg_win | 32.6156 |
| net_avg_loss | -52.1562 |
| avg_hold_time_bars | 6.5217 |
| exposure | 0.2104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
