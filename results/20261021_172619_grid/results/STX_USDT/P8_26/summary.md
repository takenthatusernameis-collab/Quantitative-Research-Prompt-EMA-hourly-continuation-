# EMA Hourly Continuation — STX/USDT P8_26

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.7103 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.8538 |
| sortino_ratio | -1.0714 |
| max_drawdown | 0.7218 |
| cagr | -0.3886 |
| net_avg_win | 51.8822 |
| net_avg_loss | -68.9382 |
| avg_hold_time_bars | 6.7977 |
| exposure | 0.2129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
